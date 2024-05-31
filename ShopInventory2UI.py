import Shopkeeper
from Settings import *

class ShopInventory2UI(pygame.sprite.Sprite):
    def __init__(self, groups, inventory, player):
        super().__init__(groups)
        self.inventory = inventory
        self.inventory_slot_size = 48
        self.player = player
        self.image = pygame.Surface((self.inventory.columns * self.inventory_slot_size, self.inventory.rows * self.inventory_slot_size))
        self.image.fill('gray')
        self.rect = self.image.get_frect(topleft=(WINDOW_WIDTH // 2, 0))
        self.font = pygame.font.Font(None, 24)
        self.slot_rects = []
        self.can_click = True
        self.selected_item = None
        self.time_since_last_click = pygame.time.get_ticks()

    def render(self):
        self.rect.topleft = (self.player.rect.right, self.player.rect.centery - WINDOW_HEIGHT // 2)
        self.image.fill('gray')
        self.slot_rects = []

        for i in range(self.inventory.columns):
            for j in range(self.inventory.rows):
                item = self.inventory.get_item(i, j)
                slot_rect = pygame.Rect(i * self.inventory_slot_size, j * self.inventory_slot_size,
                                        self.inventory_slot_size, self.inventory_slot_size)
                self.slot_rects.append(slot_rect)
                pygame.draw.rect(self.image, 'black', slot_rect, 1)
                if item != 0:
                    if self.selected_item is not None and item == self.selected_item:
                        pygame.draw.rect(self.image, 'blue', slot_rect, 2)  # Підсвічуємо синім
                        Shopkeeper.sell_equipment(item, self.player)
                        self.selected_item = None
                        continue
                    item_rect = item.image.get_rect(center=slot_rect.center)
                    self.image.blit(item.image, item_rect.topleft)
                    if item.amount > 1:
                        text_surface = self.font.render(str(item.item_type.value[1]) + "$", True, 'black')
                        text_position = (
                        slot_rect.right - text_surface.get_width() - 2, slot_rect.bottom - text_surface.get_height())
                        self.image.blit(text_surface, text_position)

        if self.selected_item:
            mouse_pos = pygame.mouse.get_pos()
            self.image.blit(self.selected_item.image, (mouse_pos[0] - WINDOW_WIDTH // 2 - 25, mouse_pos[1]))


    def selected_slot(self):
        click = pygame.mouse.get_pressed()[0]
        if click == 0:
            self.can_click = True
            return
        if not self.can_click:
            return

        mouse_pos = pygame.mouse.get_pos()
        mouse_pos = (mouse_pos[0] - WINDOW_WIDTH // 2 - 25, mouse_pos[1]) # repairs the mouse position to be relative to the inventory
        # do math to get the slot number
        slot = (mouse_pos[0] // 48, mouse_pos[1] // 48)
        if slot[0] < 0 or slot[0] >= self.inventory.columns or slot[1] < 0 or slot[1] >= self.inventory.rows:
            return
        return slot

    def mouse_logic(self):
        if pygame.time.get_ticks() - self.time_since_last_click < 200:
            return

        slot = self.selected_slot()
        if slot is None:
            return

        self.time_since_last_click = pygame.time.get_ticks()

        if self.selected_item is None:
            new_item = self.inventory.get_item(slot[0], slot[1])
            if new_item == 0:
                return
            self.selected_item = new_item
            return self.selected_item




    def update(self, dt):
        self.mouse_logic()
        self.render()
