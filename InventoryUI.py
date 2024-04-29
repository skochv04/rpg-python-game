import pygame
from Settings import *

class InventoryUI(pygame.sprite.Sprite):
    def __init__(self, groups, inventory, player):
        super().__init__(groups)
        self.inventory = inventory
        self.player = player
        self.image = pygame.Surface((WINDOW_WIDTH // 2, WINDOW_HEIGHT))
        self.image.fill('gray')
        self.rect = self.image.get_frect(topleft=(WINDOW_WIDTH // 2, 0))
        self.slot_rects = []


    def render(self):
        self.rect.topleft = (self.player.rect.right, self.player.rect.centery - WINDOW_HEIGHT // 2)
        self.image.fill('gray')
        self.slot_rects = []

        font = pygame.font.Font(None, 14)

        for i in range(self.inventory.columns):
            for j in range(self.inventory.rows):
                item = self.inventory.get_item(i, j)
                if item != 0:
                    self.image.blit(item.image, (i * 48, j * 48))
                slot_rect = pygame.Rect(i * 48, j * 48, 48, 48)
                self.slot_rects.append(slot_rect)
                pygame.draw.rect(self.image, 'black', slot_rect, 1)

                text_surface = font.render(f'{slot_rect.x}, {slot_rect.y}', True, 'black')
                self.image.blit(text_surface, (i * 48, j * 48))

    def detect_slot(self):
        event = pygame.event.poll()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pos = (mouse_pos[0] - WINDOW_WIDTH // 2 - 25, mouse_pos[1])
        else:
            return

        # do math to get the slot number
        slot = (mouse_pos[0] // 48, mouse_pos[1] // 48)
        if slot[0] < 0 or slot[0] >= self.inventory.columns or slot[1] < 0 or slot[1] >= self.inventory.rows:
            return

        print(f'Clicked slot {slot[0]}, {slot[1]}')


    def update(self, dt):
        self.detect_slot()
        self.render()