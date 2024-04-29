from Enemy import Enemy
from NPC import NPC


class Wilddog(Enemy):
    def fight(self, player):
        raise NotImplementedError
