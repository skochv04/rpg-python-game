from Quests import Quests
from NPC import NPC
from Quest import Quest


class Questgiver(NPC):
    def __init__(self, pos, groups, collision_sprites, current_dialogue, player, timer):
        super().__init__(pos, groups, collision_sprites, current_dialogue, player, timer)
        self.started_quest = False
        self.awarded_player = False
        self.done_quest = False
        self.quest_id = 0
    def action(self, player):
        if not self.done_quest:
            self.done_quest = True
            self.started_quest = False
            next_dialogue = int(self.current_dialogue) + 1
            self.current_dialogue = str(next_dialogue).zfill(len(self.current_dialogue))

    def dialogue(self):
        if self.player.player_data.quest and self.player.player_data.quest.isDone(self.player.player_data):
            self.action(self.player)
        responses, last_dialogue = super().dialogue()
        response_num = int(last_dialogue)
        print("response: ", response_num)
        if 0 < response_num < 1000 and response_num % 2:

            # start new quest
            if not self.started_quest:
                self.player.player_data.quest = Quest(self.player.player_data, list(Quests)[self.quest_id])
                self.current_dialogue = last_dialogue
                self.started_quest = True
                self.awarded_player = False
                self.quest_id += 1

        elif 0 < response_num < 1000 and not response_num % 2 and not self.awarded_player:
            # award player
            print("Award...")
            self.player.player_data.quest.rewardPlayer(self.player.player_data)
            self.awarded_player = True
