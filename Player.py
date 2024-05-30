import pygame
from PlayerData import PlayerData
from Settings import *
from Spritessheet import SpritesSheet
from InventoryUI import InventoryUI
from pygame.math import Vector2 as vector

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites, invisible_collision_sprites, player_data, name="undefined", skin=1, direction=vector(0, 0)):
        super().__init__([groups, collision_sprites])
        self.invisible_collision_sprites = invisible_collision_sprites
        self.image = pygame.Surface((42, 48))

        self.rect = self.image.get_frect(topleft=pos)
        self.old_rect = self.rect.copy()

        self.speed = 300
        self.player_data = PlayerData(100, 30, 1, skin)

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

        self.skin_action = 1
        self.skin_timer = 0
        self.prev_image = self.current_skin[1]
        self.is_moving = False

        self.is_invisible = False
        self.invisibility_start_time = None

    def input(self):
        keys = pygame.key.get_pressed()
        key_direction = vector(0, 0)
        if keys[pygame.K_RIGHT]:
            key_direction = vector(1, 0)
            self.current_skin = self.sprite_right
            self.is_moving = True
        elif keys[pygame.K_LEFT]:
            key_direction = vector(-1, 0)
            self.current_skin = self.sprite_left
            self.is_moving = True
        elif keys[pygame.K_UP]:
            key_direction = vector(0, -1)
            self.current_skin = self.sprite_up
            self.is_moving = True
        elif keys[pygame.K_DOWN]:
            key_direction = vector(0, 1)
            self.current_skin = self.sprite_down
            self.is_moving = True
        else:
            self.image = self.current_skin[1]

        if keys[pygame.K_v]:
            self.activate_invisibility()

        self.direction = key_direction

    def activate_invisibility(self):
        if not self.is_invisible:
            self.is_invisible = True
            self.invisibility_start_time = pygame.time.get_ticks()
            self.set_transparency(128)  # 50% transparency

    def deactivate_invisibility(self):
        self.is_invisible = False
        self.set_transparency(255)  # Reset transparency to 100%

    def set_transparency(self, alpha):
        for img_list in [self.sprite_down, self.sprite_left, self.sprite_right, self.sprite_up]:
            for img in img_list:
                img.set_alpha(alpha)

    def place(self, pos):
        self.rect = self.image.get_rect(topleft=pos)

    def move(self, dt):
        if self.is_moving:
            self.skin_timer = (self.skin_timer + 1) % 56
            self.is_moving = False
            if self.skin_timer == 55:
                self.skin_action = (self.skin_action + 1) % 3
                self.prev_image = self.image
                self.image = self.current_skin[self.skin_action]

        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')

    def collision(self, axis):
        if not self.is_invisible:
            for sprite in self.collision_sprites:
                if sprite.rect.colliderect(self.rect):
                    if axis == 'horizontal':
                        if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                            self.rect.left = sprite.rect.right
                        if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                            self.rect.right = sprite.rect.left
                    else:
                        if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                            self.rect.top = sprite.rect.bottom
                        if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                            self.rect.bottom = sprite.rect.top
        else:
            for sprite in self.invisible_collision_sprites:
                if sprite.rect.colliderect(self.rect):
                    if axis == 'horizontal':
                        if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                            self.rect.left = sprite.rect.right
                        if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                            self.rect.right = sprite.rect.left
                    else:
                        if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                            self.rect.top = sprite.rect.bottom
                        if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                            self.rect.bottom = sprite.rect.top

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)

        if self.is_invisible and pygame.time.get_ticks() - self.invisibility_start_time > 10000:
            self.deactivate_invisibility()