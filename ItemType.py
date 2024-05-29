from enum import Enum

from Settings import *


class ItemType(Enum):
    # id, price, damage, min_power_to_get, image
    SCISSORS = (1, 40, 15, 0, pygame.image.load(join('graphics', 'objects', 'items', 'scissors.png')))
    HAMMER = (2, 50, 20, 5, pygame.image.load(join('graphics', 'objects', 'items', 'hammer.png')))
    POISONOUS_SNAIL = (3, 60, 25, 10, pygame.image.load(join('graphics', 'objects', 'items', 'poisonous_snail.png')))
    MAGIC_STONE = (4, 80, 35, 15, pygame.image.load(join('graphics', 'objects', 'items', 'magic_stone.png')))
    SHIELD = (5, 70, 10, 20, pygame.image.load(join('graphics', 'objects', 'items', 'shield.png')))
    DIAMOND = (6, 30, 10, 0, pygame.image.load(join('graphics', 'objects', 'items', 'diamond.png')))
    FLAMMABLE_LIQUID = (7, 10, 35, 45, pygame.image.load(join('graphics', 'objects', 'items', 'flammable_liquid.png')))
    CHEMICAL_LIQUID = (8, 120, 40, 50, pygame.image.load(join('graphics', 'objects', 'items', 'chemical_liquid.png')))
    THREAD = (9, 55, 25, 8, pygame.image.load(join('graphics', 'objects', 'items', 'thread.png')))
    ACID = (10, 75, 30, 15, pygame.image.load(join('graphics', 'objects', 'items', 'acid.png')))
    SLEEPING_FLOWER = (11, 10, 20, 0, pygame.image.load(join('graphics', 'objects', 'items', 'sleeping_flower.png')))
