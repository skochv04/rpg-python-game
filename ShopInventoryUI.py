from Settings import *
import pygame

class ShopInventoryUI(pygame.sprite.Sprite):
    def __init__(self, groups, inventory, player):
        super().__init__(groups)
        self.inventory = inventory
        self.inventory.columns = 4
        self.inventory.rows = 5
        self.inventory_slot_size = 72  # Збільшений розмір слоту
        self.player = player
        self.image = pygame.Surface((self.inventory.columns * self.inventory_slot_size, self.inventory.rows * self.inventory_slot_size + 50))  # Додано місце для кнопки
        self.image.fill('gray')
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.font = pygame.font.Font(None, 24)
        self.can_click = True
        self.selected_item = None
        self.time_since_last_click = pygame.time.get_ticks()

        # Параметри кнопки "Close"
        self.close_button_rect = pygame.Rect((self.rect.width // 2 - 50, self.rect.height - 40), (100, 30))
        self.close_button_color = 'red'
        self.close_button_text = self.font.render('Close', True, 'white')

    def render(self):
        self.image.fill('gray')
        self.slot_rects = []

        for i in range(self.inventory.columns):
            for j in range(self.inventory.rows):
                item = self.inventory.get_item(i, j)
                slot_rect = pygame.Rect(i * self.inventory_slot_size, j * self.inventory_slot_size,
                                        self.inventory_slot_size, self.inventory_slot_size)
                self.slot_rects.append(slot_rect)
                # Перевірка, чи мишка наведена на клітинку інвентаря
                if slot_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(self.image, 'lightblue', slot_rect)  # Підсвічуємо клітинку якщо мишка наведена
                else:
                    pygame.draw.rect(self.image, 'black', slot_rect, 1)
                if item != 0:
                    item_rect = item.image.get_rect(center=slot_rect.center)
                    self.image.blit(item.image, item_rect.topleft)
                    if item.amount > 1:
                        text_surface = self.font.render(str(item.price) + "$", True, 'black')
                        text_position = (
                        slot_rect.right - text_surface.get_width() - 2, slot_rect.bottom - text_surface.get_height())
                        self.image.blit(text_surface, text_position)

        # Малювання кнопки "Close"
        pygame.draw.rect(self.image, self.close_button_color, self.close_button_rect)
        self.image.blit(self.close_button_text, self.close_button_text.get_rect(center=self.close_button_rect.center))


    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            # Перевірка, чи натиснуто на вікно інвентаря
            if self.rect.collidepoint(mouse_pos):
                local_mouse_pos = (mouse_pos[0] - self.rect.left, mouse_pos[1] - self.rect.top)
                # Перевірка, чи натиснуто на кнопку "Close"
                if self.close_button_rect.collidepoint(local_mouse_pos):
                    self.kill()  # Закриває вікно інвентаря

    def update(self, dt):
        self.render()