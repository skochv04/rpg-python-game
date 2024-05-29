from ItemType import ItemType
from Settings import *
from Item import Item
from Inventory import Inventory


class PlayerData:
    def __init__(self, health, coins, power):
        self.health = health
        self.coins = coins
        self.power = power
        self.skills = []
        self.inventory = Inventory()

        self.inventory.add_item(Item(ItemType.SCISSORS, 2))
        self.inventory.add_item(Item(ItemType.HAMMER, 5))
