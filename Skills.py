from enum import Enum

from Settings import *


class Skills(Enum):
    # id, price, min_exp_to_get, image, name
    SPEED_UP = (1, 80, 5, pygame.image.load(join('graphics', 'objects', 'items', 'speed_up.png')), "speed-up")
    TELEPORTATION = (
    2, 100, 10, pygame.image.load(join('graphics', 'objects', 'items', 'teleportation.png')), "teleportation")
    SHRINK = (3, 200, 15, pygame.image.load(join('graphics', 'objects', 'items', 'shrink.png')), "shrink")
    INVISIBILITY = (
    4, 300, 20, pygame.image.load(join('graphics', 'objects', 'items', 'invisibility.png')), "invisibility")

    def __str__(self):
        return self.value[0]
