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

        self.inventory.add_item(Item('Skull', 0, 'A skull', 10,
                                     pygame.image.load(join('graphics','objects', 'items', 'skull.png')), 1))
        self.inventory.add_item(Item("Gold", 5, "A golden coin", 1,
                                     pygame.image.load(join('graphics','objects', 'items', 'gold.png')), 5))