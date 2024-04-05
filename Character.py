from Vector2D import Vector2D
from MapDirection import MapDirection


class Character:
    # to choose correct images for character we will use skin and direction
    def __init__(self, skin=1, name="undefined", vector=Vector2D(0, 0), direction=MapDirection.TOP_1):
        self.name = name
        self.position = vector
        self.direction = direction
        self.skin = skin

        self.money = 100
        self.health = 100
        self.power = 1

        self.skills = []  # list of Skills enum objects

    def place(self, vector):
        self.position = vector

    def move(self, map_direction):
        self.position.add(map_direction.value[1])
        self.direction = map_direction
        return self.position

    def __str__(self):
        return self.direction.__str__()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
