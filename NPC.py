from Dialogue import Dialogue
from Settings import *
from Spritessheet import SpritesSheet
from UI import UI


class NPC(pygame.sprite.Sprite):
    def __init__(self, pos, groups, current_dialogue, player, timer):
        super().__init__(groups)
        self.image = pygame.Surface((48, 56))
        # self.image.fill('red')
        self.rect = self.image.get_frect(topleft=pos)

        self.dialogue_data = Dialogue(f'graphics/npc/{self.__class__.__name__}/dialogue.json')
        self.current_dialogue = current_dialogue
        self.start_dialogue = current_dialogue

        my_spritesheet = SpritesSheet(f'graphics/npc/{self.__class__.__name__}/texture.png')
        self.sprite_stable = [my_spritesheet.parse_sprite('1.png'), my_spritesheet.parse_sprite('2.png'),
                              my_spritesheet.parse_sprite('3.png')]

        self.current_img = 0
        self.image = self.sprite_stable[self.current_img]
        self.player = player

        self.timer = timer

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

    def update(self, dt):
        self.timer += 1
        if self.timer == 2150:
            self.current_img += 1
            self.current_img %= 3
            self.image = self.sprite_stable[self.current_img]
            self.timer = 0
        if self.timer == 2075:
            self.current_img += 1
            self.current_img %= 3
            self.image = self.sprite_stable[self.current_img]
        if self.timer == 2000:
            self.current_img += 1
            self.current_img %= 3
            self.image = self.sprite_stable[self.current_img]
        self.input()

    def action(self, player):
        raise NotImplementedError
