from Settings import *
from Spritessheet import SpritesSheet


class Player(pygame.sprite.Sprite):
    # to choose correct images for character we will use skin and direction
    def __init__(self, pos, groups, name="undefined", skin=1, direction=vector(0, 0)):
        super().__init__(groups)
        self.image = pygame.Surface((48, 56))
        # self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)

        self.pos = (pos[0], pos[1])
        self.speed = 300

        self.name = name
        self.direction = direction
        self.skin = skin

        self.money = 100
        self.health = 100
        self.power = 1

        self.skills = []  # list of Skills enum objects
        self.equipment = []

        self.move_disabled = False

        my_spritesheet = SpritesSheet(f'graphics/player/{skin}/texture.png')
        # trainer1 = my_spritesheet.get_sprite(128, 128, 128, 128).convert_alpha()
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

        # self.path = f'graphics/player/{skin}'
        # self.image = pygame.image.load(f'{self.path}/run/0.png').convert_alpha()

    def input(self):
        keys = pygame.key.get_pressed()
        key_direction = [0, 0]
        if keys[pygame.K_RIGHT]:
            key_direction = [1, 0]
            self.current_skin = self.sprite_right
        elif keys[pygame.K_LEFT]:
            key_direction = [-1, 0]
            self.current_skin = self.sprite_left
        elif keys[pygame.K_UP]:
            key_direction = [0, -1]
            self.current_skin = self.sprite_up
        elif keys[pygame.K_DOWN]:
            key_direction = [0, 1]
            self.current_skin = self.sprite_down

        # if key_direction:
        #     self.direction = key_direction.normalize()
        # else:
        #     self.direction = key_direction

        self.direction = key_direction

    def place(self, pos):
        self.rect = self.image.get_rect(topleft=pos)

    def move(self, dt):
        self.pos = (self.pos[0] + self.direction[0] * self.speed * dt, self.pos[1] + self.direction[1] * self.speed * dt)
        self.rect.topleft = self.pos
        self.image = self.current_skin[1]


    def update(self, dt):
        self.input()
        self.move(dt)

    # def __eq__(self, other):
    #     return self.position[0] == other.position[0] and self.position[1] == other.position[1]

    # def __hash__(self):
    #     return hash((self.position[0], self.position[1]))
