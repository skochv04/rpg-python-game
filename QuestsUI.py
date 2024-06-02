import pygame
from os.path import join
from Settings import WINDOW_WIDTH, WINDOW_HEIGHT


class QuestsUI(pygame.sprite.Sprite):
    def __init__(self, groups, player):
        super().__init__(groups)
        self.player = player
        self.font = pygame.font.Font(None, 36)
        if self.player.player_data.quest is None:
            self.message = "You haven`t any quests now. You can ask Questgiver about them!"
            self.ui_image = pygame.image.load(join('graphics', 'objects', 'ask.png'))
        elif self.player.player_data.quest.isDone(self.player.player_data):
            self.message = "You have completed all quest tasks. Meet the Questgiver to collect the prize and continue!"
            self.ui_image = pygame.image.load(join('graphics', 'objects', 'done.png'))
            for npc in groups:
                if npc.__class__.__name__ == 'Questgiver':
                    npc.action()
        else:
            self.message = self.player.player_data.quest.quest.value[1]
            self.additional_message = self.player.player_data.quest.quest.value[13]  # Додаємо друге повідомлення
            self.ui_image = None  # Зберігаємо зображення предмета

        # Збільшуємо ширину вікна та розміщуємо по центру екрану відносно гравця
        self.image = pygame.Surface((WINDOW_WIDTH * 0.7, WINDOW_HEIGHT * 0.7))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=(self.player.rect.centerx, self.player.rect.centery))
        self.bound = ((WINDOW_WIDTH - WINDOW_WIDTH * 0.7) // 2, (WINDOW_HEIGHT - WINDOW_HEIGHT * 0.7) // 2)

        # Створюємо кнопку
        self.button_font = pygame.font.Font(None, 24)
        self.button_text = self.button_font.render('Close', True, (255, 255, 255))
        self.button_image = pygame.Surface((100, 50))
        self.button_image.fill((0, 0, 0))
        self.button_image.blit(self.button_text, (10, 10))
        self.button_rect = self.button_image.get_rect(
            center=(self.image.get_width() - 70, self.image.get_height() - 30))

        self.item_rect = None

    def render(self):
        self.image.fill('white')

        # Якщо передано зображення предмета, відобразимо його
        if self.ui_image:
            self.item_rect = self.ui_image.get_rect(
                center=(self.image.get_width() // 2, self.image.get_height() - self.image.get_height() // 3))
            self.image.blit(self.ui_image, self.item_rect)

        # Відображення повідомлення
        text_surface = self.font.render(self.message, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.image.get_width() // 2, self.image.get_height() // 2 - 20))
        self.image.blit(text_surface, text_rect)

        # Відображення додаткового повідомлення
        if hasattr(self, 'additional_message'):
            additional_text_surface = self.font.render(self.additional_message, True, (0, 0, 0))
            additional_text_rect = additional_text_surface.get_rect(center=(self.image.get_width() // 2, self.image.get_height() // 2 + 20))
            self.image.blit(additional_text_surface, additional_text_rect)

        # Відображення кнопки
        self.image.blit(self.button_image, self.button_rect)

    def update(self, dt):
        self.input()
        self.rect.center = (self.player.rect.centerx, self.player.rect.centery)
        self.render()

    def input(self):
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if mouse_buttons[0]:
            relative_mouse_pos = (mouse_pos[0] - self.bound[0] + self.button_rect.width // 2, (mouse_pos[1] - self.bound[1]))
            if self.button_rect.collidepoint(relative_mouse_pos):
                self.kill()
