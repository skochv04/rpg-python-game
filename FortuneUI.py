import pygame
from os.path import join
from Settings import WINDOW_WIDTH, WINDOW_HEIGHT


class FortuneUI(pygame.sprite.Sprite):
    def __init__(self, groups, player, fortune, message, item_icon=None):
        super().__init__(groups)
        self.player = player
        self.fortune = fortune
        self.font = pygame.font.Font(None, 36)
        self.message = message  # Зберігаємо текст повідомлення
        self.item_icon = item_icon  # Зберігаємо зображення предмета

        # Збільшуємо ширину вікна та розміщуємо по центру екрану
        self.image = pygame.Surface((WINDOW_WIDTH * 0.7, WINDOW_HEIGHT * 0.7))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH // 1.85, WINDOW_HEIGHT // 1.7))

    def render(self):
        self.image.fill('white')

        # Якщо передано зображення предмета, відобразимо його
        if self.item_icon:
            item_rect = self.item_icon.get_rect(center=(self.image.get_width() // 2, self.image.get_height() - self.image.get_height() // 3))
            self.image.blit(self.item_icon, item_rect)

        # Відображення повідомлення
        text_surface = self.font.render(self.message, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.image.get_width() // 2, self.image.get_height() // 2))
        self.image.blit(text_surface, text_rect)


    def update(self, dt):
        self.render()
