import random

from Skills import Skills
from ItemType import ItemType
from Settings import *
from Item import Item
from Inventory import Inventory
from EntityData import EntityData
from EntityData import EntityData
from BattleSkill import *

available_items = {
    0: [ItemType.SCISSORS, ItemType.HAMMER, ItemType.POISONOUS_SNAIL],
    1: [ItemType.MAGIC_STONE, ItemType.SHIELD, ItemType.DIAMOND],
    2: [ItemType.FLAMMABLE_LIQUID, ItemType.CHEMICAL_LIQUID, ItemType.THREAD],
    3: [ItemType.ACID, ItemType.SLEEPING_FLOWER, ItemType.THREAD],
    4: [ItemType.SCISSORS, ItemType.HAMMER, ItemType.POISONOUS_SNAIL],
    5: [ItemType.MAGIC_STONE, ItemType.SHIELD, ItemType.DIAMOND],
    6: [ItemType.FLAMMABLE_LIQUID, ItemType.CHEMICAL_LIQUID, ItemType.THREAD],
    7: [ItemType.ACID, ItemType.SLEEPING_FLOWER, ItemType.THREAD]
}


class PlayerData(EntityData):

    def __init__(self, health, coins, power, magic_power, mana, itemset, audio_files, background_sound, timer=0):
        super().__init__(health, health, power, magic_power)
        self.coins = coins
        self.skills = set()
        self.battle_skills = [Heal(), Fireball()]
        self.level = 1
        self.exp = 0
        self.mana = mana
        self.inventory = Inventory()
        self.timer = timer
        self.quest = None
        self.exp = 0
        self.itemset = itemset

        self.audio_files = audio_files

        #sounds
        self.background_sound = background_sound

        self.coin_sound = audio_files['coin']
        self.coin_sound.set_volume(0.3)

        self.up_level_sound = audio_files['up_level']
        self.up_level_sound.set_volume(0.3)

        self.quest_done_sound = audio_files['quest_done']
        self.quest_done_sound.set_volume(0.45)

        self.fight_win_sound = audio_files['fight_win']
        self.fight_win_sound.set_volume(0.45)

        self.skill_activate_sound = audio_files['skill_activate']
        self.skill_activate_sound.set_volume(0.45)

        self.fortune_fail_sound = audio_files['fortune_fail']
        self.fortune_fail_sound.set_volume(0.45)

        self.fortune_coin_sound = audio_files['fortune_coin']
        self.fortune_coin_sound.set_volume(0.45)

        self.fortune_health_sound = audio_files['fortune_health']
        self.fortune_health_sound.set_volume(0.45)

        self.fortune_equipment_sound = audio_files['fortune_equipment']
        self.fortune_equipment_sound.set_volume(0.45)

        self.jump_sound = audio_files['jump']
        self.jump_sound.set_volume(0.4)

        self.timer_sound = audio_files['timer']
        self.timer_sound.set_volume(0.4)

        self.skill_small_sound = audio_files['skill_small']
        self.skill_small_sound.set_volume(0.45)

        self.mouse_click_sound = audio_files['mouse_click']
        self.mouse_click_sound.set_volume(0.45)

        self.npc_sound = audio_files['npc']
        self.npc_sound.set_volume(0.0)
        self.npc_sound.play(-1)


        # Player can earn coins only by collecting coins on map, speaking with Fortune and winning enemies
        # In these variables we don`t add earned coins in quests
        self.earned_coins_total = 0
        self.earned_coins_level = 0
        self.demand_coins_total = 0

        self.enemies_won_total = 0
        self.enemies_won_level = 0
        self.demand_enemies_won_total = 0

        if self.itemset is None:
            self.itemset = random.choice(list(available_items.keys())) + 1
        else:
            print((self.itemset - 1) % len(Skills))
        for item in available_items[self.itemset - 1]: self.inventory.add_item(Item(item, 3))

        self.skills.add(list(Skills)[(self.itemset - 1) % len(Skills)])

    def up_level(self):
        self.earned_coins_total += self.earned_coins_level
        self.enemies_won_total += self.enemies_won_level

        self.level += 1
        self.earned_coins_level = 0
        self.enemies_won_level = 0
        self.up_level_sound.play()

    def increase_coins(self, amount):
        self.coins += amount
        self.coin_sound.play()
