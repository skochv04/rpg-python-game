class PlayerData:
    def __init__(self, health, coins, power):
        self.health = health
        self.coins = coins
        self.power = power
        self.skills = []
        self.inventory = [[0 for _ in range(5)] for _ in range(4)]