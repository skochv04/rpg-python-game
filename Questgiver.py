from NPC import NPC


class Questgiver(NPC):
    def action(self, player):
        raise NotImplementedError
