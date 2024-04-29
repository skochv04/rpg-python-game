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

    def render(self):
        self.rect.topleft = (self.player.rect.right, self.player.rect.centery - WINDOW_HEIGHT // 2)
        self.image.fill('gray')

        for i in range(self.inventory.columns):
            for j in range(self.inventory.rows):
                item = self.inventory.get_item(i, j)
                if item != 0:
                    self.image.blit(item.image, (i * 48, j * 48))

    def update(self, dt):
        self.render()