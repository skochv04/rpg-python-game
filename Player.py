from Settings import *
# from Vector2D import Vector2D

class Player(pygame.sprite.Sprite):
    # to choose correct images for character we will use skin and direction
    def __init__(self, pos, groups, skin=1, name="undefined", direction=vector(0, 0)):
        super().__init__(groups)
        self.image = pygame.Surface((48, 56))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)

        self.speed = 200

        self.name = name
        self.direction = direction
        self.skin = skin

        self.money = 100
        self.health = 100
        self.power = 1

        self.skills = []  # list of Skills enum objects

    def input(self):
        keys = pygame.key.get_pressed()
        key_direction = vector(0, 0)
        if keys[pygame.K_RIGHT]:
            key_direction = vector(1, 0)
        elif keys[pygame.K_LEFT]:
            key_direction = vector(-1, 0)
        elif keys[pygame.K_UP]:
            key_direction = vector(0, -1)
        elif keys[pygame.K_DOWN]:
            key_direction = vector(0, 1)

        # if key_direction:
        #     self.direction = key_direction.normalize()
        # else:
        #     self.direction = key_direction

        self.direction = key_direction

    def place(self, pos):
        self.rect = self.image.get_rect(topleft=pos)

    def move(self, dt):
        self.rect.topleft += self.direction * self.speed * dt

    def update(self, dt):
        self.input()
        self.move(dt)

    # def __eq__(self, other):
    #     return self.position[0] == other.position[0] and self.position[1] == other.position[1]

    # def __hash__(self):
    #     return hash((self.position[0], self.position[1]))