from enum import Enum

from Settings import *


class Quests(Enum):
    # id, name, price, damage, min_power_to_get, image, name
    SCISSORS = (1, 40, 15, 0, pygame.image.load(join('graphics', 'objects', 'items', 'scissors.png')), "scissors")