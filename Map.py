import pygame.image

# import Map
from Character import Character
from Vector2D import Vector2D
from MapDirection import MapDirection


class Map:
    def __init__(self):
        self.tilesize = 16
        self.map = [["-" for _ in range(16)] for _ in range(16)]
        self.characters = {}
        self.tileset = pygame.image.load("sprites/floor/decor_8x8.png")
        self.tile_mapping = {
            # key: (x, y, width, height)
            0: (0, 0, self.tilesize, self.tilesize),
            1: (self.tilesize, 0, self.tilesize, self.tilesize)
        }

    def print_map(self):
        for y in range(self.tilesize, -1, -1):
            for x in range(self.tilesize):
                if Vector2D(x, y) in self.characters:
                    print(self.characters[Vector2D(x, y)], end=" ")
                else:
                    print("-", end=" ")
            print()

    def place(self, character, position):
        self.characters[position] = character
        character.position = position

    def remove(self, position):
        if position in self.characters:
            del self.characters[position]

    def move(self, character, map_direction):
        self.remove(character.position)
        new_position = character.move(map_direction)
        self.place(character, new_position)


radar = Map()
first = Character()
radar.place(first, Vector2D(1, 2))
radar.print_map()
print()
radar.move(first, MapDirection.LEFT_1)
radar.print_map()
