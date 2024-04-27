from Dialogue import Dialogue
from NPC import NPC
from Settings import *
from UI import UI


def sell_equipment(equipment, player):
    if player.money >= equipment.price:
        player.money -= equipment.price
        player.equipment += [equipment]
        return True
    return False


class Shopkeeper(NPC):
    def __init__(self, pos, groups, current_dialogue, player):
        super().__init__(pos, groups, current_dialogue, player)
        self.last_input_time = 0
        self.time_between_inputs = 200

    def dialogue(self):
        ui = UI(self.dialogue_data, self.current_dialogue)
        ui.run()
        self.last_input_time = pygame.time.get_ticks()


    def is_active(self):
        player_pos, self_pos = vector(self.player.rect.center), vector(self.rect.center)
        in_range = self_pos.distance_to(player_pos) < 100

        return in_range

    def input(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_input_time >= self.time_between_inputs:
            if self.is_active():
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    self.dialogue()

    def action(self, player):
        raise NotImplementedError

    def update(self, dt):
        self.input()
