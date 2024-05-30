import random

from Skills import Skills
from ItemType import ItemType
from Settings import *
from Item import Item
from Inventory import Inventory

available_items = {
    0: [ItemType.SCISSORS, ItemType.HAMMER, ItemType.POISONOUS_SNAIL],
    1: [ItemType.MAGIC_STONE, ItemType.SHIELD, ItemType.DIAMOND],
    2: [ItemType.FLAMMABLE_LIQUID, ItemType.CHEMICAL_LIQUID, ItemType.THREAD],
    3: [ItemType.ACID, ItemType.SLEEPING_FLOWER, ItemType.THREAD],
    4: [ItemType.SCISSORS, ItemType.HAMMER, ItemType.POISONOUS_SNAIL],
    5: [ItemType.MAGIC_STONE, ItemType.SHIELD, ItemType.DIAMOND],
    6: [ItemType.FLAMMABLE_LIQUID, ItemType.CHEMICAL_LIQUID, ItemType.THREAD],
    7: [ItemType.ACID, ItemType.SLEEPING_FLOWER, ItemType.THREAD]
}


class PlayerData:

    def __init__(self, health=100, coins=30, power=1, itemset=None):
        self.health = health
        self.coins = coins
        self.power = power
        self.skills = []
        self.inventory = Inventory()

        if itemset is None:
            itemset = random.choice(list(available_items.keys())) + 1
        else:
            print((itemset - 1) % len(Skills))
        for item in available_items[itemset - 1]: self.inventory.add_item(Item(item, 3))

        self.skills.append(list(Skills)[(itemset - 1) % len(Skills)])
