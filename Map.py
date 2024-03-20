import pygame.image


class Map:
    def __init__(self):
        self.tilesize = 16
        self.map = [[0 for _ in range(32)] for _ in range(32)]
        self.tileset = pygame.image.load("sprites/floor/decor_8x8.png")
        self.tile_mapping = {
            # key: (x, y, width, height)
            0: (0, 0, self.tilesize, self.tilesize),
            1: (self.tilesize, 0, self.tilesize, self.tilesize)
        }
        