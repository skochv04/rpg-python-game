from PlayerData import PlayerData


class Quest:
    def __init__(self, player_data, quest):
        self.quest = quest
        player_data.demand_coins_total += self.quest.value[10]
        player_data.demand_enemies_won_total += self.quest.value[9]
        self.start_player_data = PlayerData(player_data.health, player_data.coins, player_data.power, player_data.magic_power, player_data.mana, player_data.itemset, player_data.audio_files)
        self.specific_cond = False

    def isDone(self, player_data):
        if player_data.enemies_won_level < player_data.demand_enemies_won_total: return False
        for item in self.quest.value[11]:
            old_amount = self.start_player_data.inventory.find_item_amount(item)
            new_amount = player_data.inventory.find_item_amount(item)
            if old_amount + item.amount > new_amount: return False
        if player_data.earned_coins_level < player_data.demand_coins_total: return False

        if self.quest.value[12] and not self.specific_cond: return False
        return True

    def rewardPlayer(self, player_data):
        player_data.exp += self.quest.value[3]
        player_data.coins += self.quest.value[4]
        player_data.health = min(player_data.health + self.quest.value[5], 100)
        for item in self.quest.value[6]:
            player_data.inventory.add_item(item)
        for skill in self.quest.value[7]:
            player_data.skills.add(skill)