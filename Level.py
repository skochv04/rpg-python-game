import pygame.sprite

from Fortune import Fortune
from Informator import Informator
from Questgiver import Questgiver
from Settings import *
from Shopkeeper import Shopkeeper
from Sprites import Sprite
from Player import Player
from AllSprites import AllSprites
from UI import UI


class Level:
    def __init__(self, tmx_map, player_name, current_skin, player_data):
        self.player_name = None
        self.display_surface = pygame.display.get_surface()

        self.player_name = player_name
        self.current_skin = current_skin
        self.player_data = player_data

        # groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()

        self.player = None

        self.setup(tmx_map)

    def setup(self, tmx_map):
        for x, y, surf in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf,(self.all_sprites, self.collision_sprites))

        for obj in tmx_map.get_layer_by_name('Objects'):
            if obj.name == 'player':
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites, self.player_name, self.current_skin)
            elif obj.name == 'shopkeeper':
                Shopkeeper((obj.x, obj.y), self.all_sprites,  "000", self.player, 0)
            elif obj.name == 'questgiver':
                Questgiver((obj.x, obj.y), self.all_sprites, "000", self.player, 500)
            elif obj.name == 'informator':
                Informator((obj.x, obj.y), self.all_sprites, "000", self.player, 1000)
            elif obj.name == 'fortune':
                Fortune((obj.x, obj.y), self.all_sprites, "000", self.player, 1500)

    def run(self, dt):
        self.all_sprites.update(dt)
        self.display_surface.fill('yellow')
        self.all_sprites.draw(self.player.rect.center)
