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
        mouse = pygame.mouse.get_pos()
        mouse = (mouse[0] - WINDOW_WIDTH//2 - 25, mouse[1])
        display_surface = pygame.display.get_surface()
        font = pygame.font.Font(None, 24)
        font_surface = font.render(f'{mouse}', True, 'black')
        display_surface.blit(font_surface, (10, 10))

        for i, slot in enumerate(self.slot_rects):
            if slot.collidepoint(mouse):
                print(f"slot {i} clicked")
                return i


    def update(self, dt):
        self.detect_slot()
        self.render()