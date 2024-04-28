from Inventory import Inventory

class PlayerData:
    def __init__(self, health, coins, power):
        self.health = health
        self.coins = coins
        self.power = power
        self.skills = []
        self.inventory = Inventory()