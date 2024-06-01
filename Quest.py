class Quest:
    def __init__(self, start_player_data, quest):
        self.start_player_data = start_player_data
        self.quest = quest

    def isDone(self, player_data):
        isDone = True
        if self.start_player_data.coins + self.quest.value[8] < player_data.coins: isDone = False
        #analogicznie
        
        return isDone