from copy import deepcopy

class Quest:
    def __init__(self, player_data, quest):
        self.start_player_data = player_data
        self.quest = quest
        self.specific_cond = False

    def isDone(self, player_data):
        if self.start_player_data.enemiesWon + self.quest.value[9] > player_data.enemiesWon: return False
        if self.start_player_data.coins + self.quest.value[10] > player_data.coins: return False
        for item in self.quest.value[11]:
            old_amount = self.start_player_data.inventory.find_item_amount(item)
            new_amount = player_data.inventory.find_item_amount(item)
            print(item, old_amount, new_amount)
            if old_amount + item.amount > new_amount: return False
        if self.quest.value[12] and not self.specific_cond: return False
        return True

    def rewardPlayer(self, player_data):
        player_data.exp += self.quest.value[3]
        player_data.coins += self.quest.value[4]
        player_data.health = min(player_data.health + self.quest.value[5], 100)
        for item in self.quest.value[5]:
            player_data.inventory.add_item(item)
        for skill in self.quest.value[6]:
            player_data.skills.add(skill)