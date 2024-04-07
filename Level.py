from Settings import *
from Sprites import Sprite
from Player import Player


class Level:
    def __init__(self, tmx_map, player_name, current_skin):
        self.player_name = None
        self.display_surface = pygame.display.get_surface()

        self.player_name = player_name
        self.current_skin = current_skin

        # groups
        self.all_sprites = pygame.sprite.Group()

        self.setup(tmx_map)

    def setup(self, tmx_map):
        for x, y, surf in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Objects'):
            if obj.name == 'player':
                Player((obj.x, obj.y), self.all_sprites, self.player_name, self.current_skin)

    def run(self, dt):
        self.all_sprites.update(dt)
        self.display_surface.fill('yellow')
        self.all_sprites.draw(self.display_surface)
