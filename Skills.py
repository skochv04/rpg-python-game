from enum import Enum
from Settings import *
import pygame

class Skills(Enum):
    SPEED_UP = (1, 80, 5, pygame.image.load(join('graphics', 'objects', 'items', 'speed_up.png')), "speed-up", "Press F")
    TELEPORTATION = (2, 100, 10, pygame.image.load(join('graphics', 'objects', 'items', 'teleportation.png')), "teleportation", "Press T and click")
    SHRINK = (3, 200, 15, pygame.image.load(join('graphics', 'objects', 'items', 'shrink.png')), "shrink", "Press S")
    INVISIBILITY = (4, 300, 20, pygame.image.load(join('graphics', 'objects', 'items', 'invisibility.png')), "invisibility", "Press V")

    @property
    def id(self):
        return self.value[0]

    @property
    def price(self):
        return self.value[1]

    @property
    def min_exp_to_get(self):
        return self.value[2]

    @property
    def image(self):
        return self.value[3]

    @property
    def name(self):
        return self.value[4]

    @property
    def keyboard(self):
        return self.value[5]

    def __str__(self):
        return str(self.id)