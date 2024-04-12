from Dialogue import Dialogue
from Settings import *


class NPC(pygame.sprite.Sprite):
    def __init__(self, pos, groups, current_dialogue):
        super().__init__(groups)
        self.image = pygame.Surface((48, 56))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)

        self.dialogue_data = Dialogue(f'graphics/npc/{self.__class__.__name__}/dialogue.json')
        self.current_dialogue = current_dialogue
        self.start_dialogue = current_dialogue

        self.dialogue()

    def dialogue(self):
        raise NotImplementedError

    def action(self, player):
        raise NotImplementedError
