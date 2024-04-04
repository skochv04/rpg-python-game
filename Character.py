from Vector2D import Vector2D
from MapDirection import MapDirection


class Character:

    def __init__(self, vector=Vector2D(0, 0), direction=MapDirection.TOP_1):
        self.position = vector
        self.direction = direction
        self.money = 100
        self.skin = 1
        self.weapon = []

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