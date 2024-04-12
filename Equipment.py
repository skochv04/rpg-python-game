from enum import Enum


class Equipment(Enum):
    SWORD = ("Sword", 50, 10)  # Name, Price, Damage
    SHIELD = ("Shield", 30, 5)
    BOW = ("Bow", 40, 8)
    ARMOR = ("Armor", 60, 0)  # Armor might not deal damage

    def __init__(self, name, price, damage):
        self.name = name
        self.price = price
        self.damage = damage

    def __str__(self):
        return f"{self.name} - Price: {self.price}, Damage: {self.damage}"
