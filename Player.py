import pygame

from Settings import *
from Spritessheet import SpritesSheet
from InventoryUI import InventoryUI

class Player(pygame.sprite.Sprite):
    # to choose correct images for character we will use skin and direction
    def __init__(self, pos, groups, collision_sprites, player_data, name="undefined", skin=1):
        super().__init__(groups)
        self.image = pygame.Surface((48, 56))

        self.rect = self.image.get_frect(topleft=pos)
        self.old_rect = self.rect.copy()

        self.speed = 300
        self.player_data = player_data

        self.collision_sprites = collision_sprites

        self.name = name
        self.direction = None
        self.skin = skin

        self.move_disabled = False

        my_spritesheet = SpritesSheet(f'graphics/player/{skin}/texture.png')
        self.sprite_down = [my_spritesheet.parse_sprite('1.png'), my_spritesheet.parse_sprite('2.png'),
                            my_spritesheet.parse_sprite('3.png')]
        self.sprite_left = [my_spritesheet.parse_sprite('4.png'), my_spritesheet.parse_sprite('5.png'),
                            my_spritesheet.parse_sprite('6.png')]
        self.sprite_right = [my_spritesheet.parse_sprite('7.png'), my_spritesheet.parse_sprite('8.png'),
                             my_spritesheet.parse_sprite('9.png')]
        self.sprite_up = [my_spritesheet.parse_sprite('10.png'), my_spritesheet.parse_sprite('11.png'),
                          my_spritesheet.parse_sprite('12.png')]

        self.current_skin = self.sprite_down
        self.image = self.current_skin[1]


    def input(self):
        keys = pygame.key.get_pressed()
        key_direction = vector(0, 0)
        if keys[pygame.K_RIGHT]:
            key_direction = vector(1, 0)
            self.current_skin = self.sprite_right
        elif keys[pygame.K_LEFT]:
            key_direction = vector(-1, 0)
            self.current_skin = self.sprite_left
        elif keys[pygame.K_UP]:
            key_direction = vector(0, -1)
            self.current_skin = self.sprite_up
        elif keys[pygame.K_DOWN]:
            key_direction = vector(0, 1)
            self.current_skin = self.sprite_down

        self.direction = key_direction

    def place(self, pos):
        self.rect = self.image.get_rect(topleft=pos)

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')

        self.image = self.current_skin[1]

    def collision(self, axis):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if axis == 'horizontal':
                    # lewo
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right

                    # prawo
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left

                else:
                    # gora
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom

                    # dol
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top


    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)

    # def __eq__(self, other):
    #     return self.position[0] == other.position[0] and self.position[1] == other.position[1]

    # def __hash__(self):
    #     return hash((self.position[0], self.position[1]))
