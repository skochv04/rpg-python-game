import pygame.freetype

from Settings import *

class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.sprites = pygame.sprite.Group()

    def show_text(self, text):
        self.sprites.empty()
        dialogue_box = Dialogue_Box()
        self.sprites.add(dialogue_box.display(text))
        self.update()
        pygame.display.flip()

    def clear_sprites(self):
        self.sprites.empty()

    def update(self):
        self.sprites.draw(self.display_surface)


class Inventory:
    def __init__(self):
        pass


class Dialogue_Box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT/4))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_frect(topleft= (0, WINDOW_HEIGHT*3/4))

    def display(self, text):
        font = pygame.freetype.Font(None, 36)
        text_surface, _ = font.render(text, 'white', 'black')
        self.image.blit(text_surface, (10, 10))
        return self
