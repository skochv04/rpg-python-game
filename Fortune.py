from enum import Enum
import random

from ItemType import ItemType
from Item import Item
from NPC import NPC
from PlayerData import available_items


class Fortune(NPC):
    health_set = [5, 10, 15, 20, 25]
    coins_set = [5, 5, 5, 5, 5, 5, 10, 10, 10, 15, 15, 15, 15, 15, 15, 20, 20, 150]

    def action(self, player):
        message = ''
        if player.player_data.coins - 20 < 0:
            message = "You don`t have 20 coins to try your luck. Earn more money and come later!"
            print(message)
            return message

        player.player_data.coins -= 20

        # 0 - nothing, 1 - health, 2 - coins, 3 - equipment
        random_number = random.randint(0, 3)
        item_types = list(ItemType)
        match random_number:
            case 0:
                message = "I regret to inform you, that fortune isn`t on your side today. You have got no presents."
            case 1:
                random_health = random.randint(0, 4)
                player.player_data.health = min(player.player_data.health + self.health_set[random_health], 100)
                message = f"You receive some vitamins to stay healthy! Your XP has risen by {self.health_set[random_health]}."
            case 2:
                random_coins = random.randint(0, 18)
                player.player_data.coins += self.coins_set[random_coins]
                message = f"Wow! You are going to be rich. {self.coins_set[random_coins]} coins for you!"
            case 3:
                random_element = random.choice(item_types)
                random_amount = random.randint(1, 5)
                player.player_data.inventory.add_item(Item(random_element, random_amount))
                message = f"It seems to me, that {random_element.value[5]} will be very useful for your missions!"
        print(message)
        self.current_dialogue = '003'
        return message

    def dialogue(self):
        responses = super().dialogue()
        if responses[0] == 0:
            self.action(self.player)