import pygame
from Settings import *

class InventoryUI(pygame.sprite.Sprite):
    def __init__(self, groups, inventory):
        super().__init__(groups)
        self.inventory = inventory
        self.image = pygame.Surface((WINDOW_WIDTH // 2, WINDOW_HEIGHT))
        self.image.fill('gray')
        self.rect = self.image.get_rect(topleft=(WINDOW_WIDTH // 2, 0))

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_i]:
            self.render()

    def render(self):
        self.image.fill('gray')
        for i in range(self.inventory.columns):
            for j in range(self.inventory.rows):
                item = self.inventory.get_item(i, j)
                if item != 0:
                    self.image.blit(item.image, (i * 48, j * 48))

    def update(self, dt):
        self.input()