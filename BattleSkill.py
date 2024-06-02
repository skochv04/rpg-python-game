import math

from Settings import *

class BattleSkill:
    def __init__(self, power, mana_cost):
        self.power = power
        self.mana_cost = mana_cost

    def validation(self, player):
        if player.player_data.mana < self.mana_cost:
            return False
        return True
    def use(self, player, enemy):
        raise NotImplementedError("Skill not implemented yet")


class Heal(BattleSkill):
    def __init__(self):
        super().__init__(2, 3)

    def use(self, player, _enemy):
        if not self.validation(player):
            return False
        player.player_data.mana -= self.mana_cost

        player.player_data.health += self.power + math.ceil(player.player_data.magic_power * 0.1)
        if player.player_data.health > player.player_data.max_health:
            player.player_data.health = player.player_data.max_health

class Fireball(BattleSkill):
    def __init__(self):
        super().__init__(2, 4)

    def use(self, player, enemy):
        if not self.validation(player):
            return False
        player.player_data.mana -= self.mana_cost
        enemy.enemy_data.health -= self.power + math.ceil(player.player_data.magic_power * 0.2)
        if enemy.enemy_data.health <= 0:
            return True
        return False

class Protect(BattleSkill):
    def __init__(self):
        super().__init__(0, 2)

    def use(self, player, _enemy):
        if not self.validation(player):
            return False
        player.player_data.mana -= self.mana_cost

        player.status_effects.protected = True
