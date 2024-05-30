import pygame.freetype
import pygame.image
from os.path import join
from Settings import *
from InventoryUI import InventoryUI

class GeneralUI:
    def __init__(self, groups, player_data, player):
        self.display_surface = pygame.display.get_surface()
        self.player_data = player_data
        self.player = player
        self.groups = groups

        self.inventory = None
        self.last_input = pygame.time.get_ticks()

        # Шрифт для відображення тексту
        self.font = pygame.freetype.Font(None, 30)

        # Завантаження іконок
        self.coin_icon = pygame.image.load(join('graphics', 'objects', 'coin.png')).convert_alpha()
        self.power_icon = pygame.image.load(join('graphics', 'objects', 'power.png')).convert_alpha()  # Приклад шляху до іконки сили
        self.health_icon = pygame.image.load(join('graphics', 'objects', 'health.png')).convert_alpha()  # Приклад шляху до іконки здоров'я

    def create_inventory(self):
        self.inventory = InventoryUI(self.groups, self.player.player_data.inventory, self.player)

    def input(self):
        keys = pygame.key.get_pressed()
        if pygame.time.get_ticks() - self.last_input < 190:
            return
        if keys[pygame.K_i] and self.inventory is None:
            self.create_inventory()
        elif keys[pygame.K_i] and self.inventory is not None:
            self.inventory.kill()
            self.inventory = None

        self.last_input = pygame.time.get_ticks()

    def update(self, dt):
        self.input()
        if self.inventory is not None:
            self.inventory.update(dt)
        # Оновлення і відображення кількості монет, сили і здоров'я
        self.render_coins()
        self.render_power()
        self.render_health()

    def render_coins(self):
        # Оновлення тексту з кількістю монет
        coin_text = str(self.player_data.coins)
        coin_surface, coin_rect = self.font.render(coin_text, 'white')

        # Позиція іконки та тексту монет
        coin_icon_rect = self.coin_icon.get_rect(topleft=(WINDOW_WIDTH - 200, 30))

        # Центрування тексту по вертикалі відносно іконки
        coin_rect.midleft = (coin_icon_rect.right + 5, coin_icon_rect.centery)

        # Відображення іконки та тексту на екрані
        self.display_surface.blit(self.coin_icon, coin_icon_rect)
        self.display_surface.blit(coin_surface, coin_rect)

    def render_power(self):
        # Оновлення тексту з рівнем сили
        power_text = str(self.player_data.power)
        power_surface, power_rect = self.font.render(power_text, 'white')

        # Позиція іконки та тексту сили
        power_icon_rect = self.power_icon.get_rect(topleft=(WINDOW_WIDTH - 100, 30))

        # Центрування тексту по вертикалі відносно іконки
        power_rect.midleft = (power_icon_rect.right + 5, power_icon_rect.centery)

        # Відображення іконки та тексту на екрані
        self.display_surface.blit(self.power_icon, power_icon_rect)
        self.display_surface.blit(power_surface, power_rect)

    def render_health(self):
        # Оновлення тексту з рівнем здоров'я
        health_text = str(self.player_data.health)
        health_surface, health_rect = self.font.render(health_text, 'white')

        # Позиція іконки та тексту здоров'я
        health_icon_rect = self.health_icon.get_rect(topleft=(30, 30))

        # Центрування тексту по вертикалі відносно іконки
        health_rect.midleft = (health_icon_rect.right + 5, health_icon_rect.centery)

        # Відображення іконки та тексту на екрані
        self.display_surface.blit(self.health_icon, health_icon_rect)
        self.display_surface.blit(health_surface, health_rect)
