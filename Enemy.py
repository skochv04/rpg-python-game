from PlayerData import PlayerData
from Settings import *
from Spritessheet import SpritesSheet
from UI import UI
from Fight import fight


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites, player, timer):
        super().__init__([groups, collision_sprites])
        self.image = pygame.Surface((32, 32))
        # self.image.fill('red')
        self.rect = self.image.get_frect(topleft=pos)
        self.old_rect = self.rect.copy()

        my_spritesheet = SpritesSheet(f'graphics/enemies/{self.__class__.__name__}/texture.png')
        self.sprite_down = [my_spritesheet.parse_sprite('1.png'), my_spritesheet.parse_sprite('2.png'),
                            my_spritesheet.parse_sprite('3.png')]
        self.sprite_left = [my_spritesheet.parse_sprite('4.png'), my_spritesheet.parse_sprite('5.png'),
                            my_spritesheet.parse_sprite('6.png')]
        self.sprite_right = [my_spritesheet.parse_sprite('7.png'), my_spritesheet.parse_sprite('8.png'),
                             my_spritesheet.parse_sprite('9.png')]
        self.sprite_up = [my_spritesheet.parse_sprite('10.png'), my_spritesheet.parse_sprite('11.png'),
                          my_spritesheet.parse_sprite('12.png')]

        self.current_skin = self.sprite_right
        self.image = self.current_skin[1]
        self.direction = vector(1, 0)

        self.player = player
        self.enemy_data = PlayerData(100, 5, 1)

        self.speed = 30
        self.collision_sprites = collision_sprites
        self.timer = timer

        self.last_input_time = 0
        self.time_between_inputs = 200

        self.skin_action = 1
        self.skin_timer = 0
        self.prev_image = self.current_skin[1]
        self.is_moving = False

    def is_active(self):
        player_pos, self_pos = vector(self.player.rect.center), vector(self.rect.center)
        in_range = self_pos.distance_to(player_pos) < 50

        return in_range

    def input(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_input_time >= self.time_between_inputs:
            if self.is_active():
                # keys = pygame.key.get_pressed()
                # if keys[pygame.K_f]:
                #     fight(self, self.player)
                fight(self, self.player)

    def move(self, dt):
        self.skin_timer = (self.skin_timer + 1) % 56
        if self.skin_timer == 55:
            self.skin_action = (self.skin_action + 1) % 3
            self.prev_image = self.image
            self.image = self.current_skin[self.skin_action]

        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)

    def opposite_direction(self, direction):
        if direction == vector(0, 1):
            self.direction = vector(0, -1)
            self.current_skin = self.sprite_down
        elif direction == vector(0, -1):
            self.direction = vector(0, 1)
            self.current_skin = self.sprite_up
        elif direction == vector(1, 0):
            self.direction = vector(-1, 0)
            self.current_skin = self.sprite_left
        elif direction == vector(-1, 0):
            self.direction = vector(1, 0)
            self.current_skin = self.sprite_right

    def collision(self, axis):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if axis == 'horizontal':
                    # lewo
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                        self.opposite_direction(self.direction)

                    # prawo
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                        self.opposite_direction(self.direction)

                else:
                    # gora
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                        self.opposite_direction(self.direction)

                    # dol
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                        self.opposite_direction(self.direction)
