from enum import Enum

from Settings import *


class ItemType(Enum):
    # id, name, price, damage, min_power_to_get, image, name
    SCISSORS = (1, 40, 15, 0, pygame.image.load(join('graphics', 'objects', 'items', 'scissors.png')), "scissors")
    HAMMER = (2, 50, 20, 5, pygame.image.load(join('graphics', 'objects', 'items', 'hammer.png')), "hammer")
    POISONOUS_SNAIL = (3, 60, 25, 10, pygame.image.load(join('graphics', 'objects', 'items', 'poisonous_snail.png')), "poisonous snail")
    MAGIC_STONE = (4, 80, 35, 15, pygame.image.load(join('graphics', 'objects', 'items', 'magic_stone.png')), "magic stone")
    SHIELD = (5, 70, 10, 20, pygame.image.load(join('graphics', 'objects', 'items', 'shield.png')), "shield")
    DIAMOND = (6, 30, 10, 0, pygame.image.load(join('graphics', 'objects', 'items', 'diamond.png')), "diamond")
    FLAMMABLE_LIQUID = (7, 10, 35, 45, pygame.image.load(join('graphics', 'objects', 'items', 'flammable_liquid.png')), "flammable liquid")
    CHEMICAL_LIQUID = (8, 120, 40, 50, pygame.image.load(join('graphics', 'objects', 'items', 'chemical_liquid.png')), "chemical liquid")
    THREAD = (9, 55, 25, 8, pygame.image.load(join('graphics', 'objects', 'items', 'thread.png')), "thread")
    ACID = (10, 75, 30, 15, pygame.image.load(join('graphics', 'objects', 'items', 'acid.png')), "acid")
    SLEEPING_FLOWER = (11, 10, 20, 0, pygame.image.load(join('graphics', 'objects', 'items', 'sleeping_flower.png')), "sleeping flower")

