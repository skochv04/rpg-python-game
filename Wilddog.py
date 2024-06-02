from Enemy import Enemy
from EntityData import EntityData


class Wilddog(Enemy):
    def __init__(self, pos, groups, collision_sprites, player, timer, power, max_health, health = None):
        super().__init__(pos, groups, collision_sprites, player, timer)
        if health is None:
            health = max_health
        self.enemy_data = EntityData(health, max_health, power)
        self.lastx = 0

    def fight_ai(self, player):
        if not self.process_status_effects(player):
            return False

        player.player_data.health -= self.enemy_data.damage
        self.enemy_data.damage = 0
        if player.player_data.health <= 0:
            return True
