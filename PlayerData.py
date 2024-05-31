from Settings import *
from Item import Item
from Inventory import Inventory
from EntityData import EntityData

class PlayerData(EntityData):
    def __init__(self, health, max_health, power, coins, skills = None):
        super().__init__(health, max_health, power, skills)
        self.coins = coins
        self.level = 1
        self.exp = 0
        self.inventory = Inventory()

        self.inventory.add_item(Item('Skull', 0, 'A skull', 10,
                                     pygame.image.load(join('graphics','objects', 'items', 'skull.png')), 1, True))
        self.inventory.add_item(Item("Gold", 5, "A golden coin", 1,
                                     pygame.image.load(join('graphics','objects', 'items', 'gold.png')), 5))