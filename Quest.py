from copy import deepcopy

from PlayerData import PlayerData


class Quest:
    def __init__(self, player_data, quest):
        print(player_data.inventory.inventory[0][0].item_type)
        print(player_data.inventory.inventory[0][1].item_type)
        print(player_data.inventory.inventory[0][2].item_type)
        self.start_player_data = PlayerData(player_data)
        print(self.start_player_data.inventory.inventory[0][0].item_type)
        print(self.start_player_data.inventory.inventory[0][1].item_type)
        print(self.start_player_data.inventory.inventory[0][2].item_type)
        self.quest = quest
        self.specific_cond = False

    def isDone(self, player_data):
        costs = 0
        if player_data.enemiesWon - self.start_player_data.enemiesWon < self.quest.value[9]: return False
        for item in self.quest.value[11]:
            old_amount = self.start_player_data.inventory.find_item_amount(item)
            new_amount = player_data.inventory.find_item_amount(item)
            print(item, old_amount, new_amount)
            costs += item.item_type.value[1]
            if old_amount + item.amount > new_amount: return False
        if player_data.coins + costs - self.start_player_data.coins < self.quest.value[10]: return False

        if self.quest.value[12] and not self.specific_cond: return False
        return True

    def rewardPlayer(self, player_data):
        print("REWARDING...")
        player_data.exp += self.quest.value[3]
        player_data.coins += self.quest.value[4]
        player_data.health = min(player_data.health + self.quest.value[5], 100)
        for item in self.quest.value[5]:
            player_data.inventory.add_item(item)
        for skill in self.quest.value[6]:
            player_data.skills.add(skill)