from enum import Enum
from random import random

import ItemType
from Item import Item
from NPC import NPC
from PlayerData import available_items


class Fortune(NPC):
    health_set = [5, 10, 15, 20, 25]
    coins_set = [5, 5, 5, 5, 5, 5, 10, 10, 10, 15, 15, 15, 15, 15, 15, 20, 20, 150]
    def action(self, player):
        #0 - nothing, 1 - health, 2 - coins, 3 - equipment
        random_number = random.randint(0, 4)
        message = ''
        match random_number:
            case 0:
                message: "I regret to inform you, that fortune isn`t on your side today. You have got no presents."
            case 1:
                random_helth = random.randint(0, 5)
                player.player_data.health += self.health_set[random_helth]
                message: f"You receive some vitamins to stay health! In has risen your XP by {Fortune.health_set[random_helth]}"
            case 2:
                random_coins = random.randint(0, 18)
                player.player_data.coins += self.coins_set[random_coins]
                message: f"Wow! You are goin to be rich. {Fortune.health_set[random_coins]} for you!"
            case 3:
                random_element = random.randint(0, 7)
                random_amount = random.randint(1, 5)
                player.player_data.inventory.add_item(Item(ItemType[random_element], random_amount))
                message: f"It seems to me, that {ItemType[random_element][5]} will be very useful to your missions!"

        self.current_dialogue = '003'
        return message
