from Dialogue import Dialogue
from NPC import NPC
from Settings import *


def sell_equipment(equipment, player):
    if player.money >= equipment.price:
        player.money -= equipment.price
        player.equipment += [equipment]
        return True
    return False


class Shopkeeper(NPC):
    def __init__(self, pos, groups, current_dialogue, player, ui):
        super().__init__(pos, groups, current_dialogue, player, ui)

    def dialogue(self):
        text, responses = self.dialogue_data.parse_text(self.current_dialogue)
        self.ui.show_text(text)
        print("\n ### " + self.__class__.__name__.upper() + ": " + text + "\n")
        if not responses:
            self.current_dialogue = self.start_dialogue
            return
        a = (list(responses.keys())[0])
        b = (list(responses.keys())[1])
        t = None
        while t != 1 and t != 2:
            print("Option 1: " + a, ", Option 2: " + b)
            print("Which option 1/2?")
            t = input()
            if t.isdigit(): t = int(t)

        selected_response = list(responses.keys())[t - 1]
        if responses[selected_response]['next'] is not None:
            self.current_dialogue = responses[selected_response]['next']
            self.dialogue()
        else:
            self.current_dialogue = self.start_dialogue
        self.ui.clear_sprites()

    def is_active(self):
        player_pos, self_pos = vector(self.player.rect.center), vector(self.rect.center)
        in_range = self_pos.distance_to(player_pos) < 100

        return in_range

    def input(self):
        if self.is_active():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                self.dialogue()

    def action(self, player):
        raise NotImplementedError

    def update(self, dt):
        self.input()
