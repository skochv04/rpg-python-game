from enum import Enum
import random
from os.path import join

from Quests import Quests
from FortuneUI import FortuneUI
from ItemType import ItemType
from Item import Item
from NPC import NPC
from PlayerData import available_items

from enum import Enum
import random
import pygame
from FortuneUI import FortuneUI
from ItemType import ItemType
from Item import Item
from NPC import NPC
from PlayerData import available_items


class Fortune(NPC):
    def __init__(self, pos, groups, collision_sprites, current_dialogue, player, timer):
        super().__init__(pos, groups, collision_sprites, current_dialogue, player, timer)
        self.FortuneUI = None

    health_set = [5, 10, 15, 20, 25]
    coins_set = [5, 5, 5, 5, 5, 5, 10, 10, 10, 15, 15, 15, 15, 15, 15, 20, 20, 150]

    def action(self):
        message = ''
        item_icon = None

        if self.player.player_data.coins - 20 < 0:
            message = "You don't have 20 coins to try your luck. Earn more money and come later!"
        else:

            self.player.player_data.coins -= 20
            self.player.player_data.quest.costs += 20

            # 0 - nothing, 1 - health, 2 - coins, 3 - equipment
            random_number = random.randint(0, 3)
            item_types = list(ItemType)
            if random_number == 0:
                message = "Oh no, fortune isn't on your side today. You have got no presents."
            elif random_number == 1:
                random_health = random.randint(0, 4)
                self.player.player_data.health = min(self.player.player_data.health + self.health_set[random_health], 100)
                message = f"You receive some vitamins to stay healthy! Your XP has been risen by {self.health_set[random_health]}."
                item_icon = pygame.image.load(join('graphics', 'objects', 'health.png')).convert_alpha()
            elif random_number == 2:
                random_coins = random.randint(0, 17)
                self.player.player_data.coins += self.coins_set[random_coins]
                message = f"Wow! You are going to be rich. {self.coins_set[random_coins]} coins for you!"
                item_icon = pygame.image.load(join('graphics', 'objects', 'coin.png')).convert_alpha()
            elif random_number == 3:
                random_element = random.choice(item_types)
                random_amount = random.randint(1, 5)
                self.player.player_data.inventory.add_item(Item(random_element, random_amount))
                message = f"It seems to me, that {random_amount} {random_element.value[5]} will be useful for your missions!"
                item_icon = random_element.value[4]
                self.current_dialogue = '003'
            if self.player.player_data.quest is not None and self.player.player_data.quest.quest == Quests.MAGIC_DUEL:
                self.player.player_data.quest.specific_cond = True
        self.FortuneUI = FortuneUI(self.groups, self.player, self, message, item_icon)

    def dialogue(self):
        responses, last_dialogue = super().dialogue()
        if len(responses) > 0 and responses[0] == 0:
            self.action()