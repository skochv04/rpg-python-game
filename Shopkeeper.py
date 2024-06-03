from Quests import Quests
from Inventory import Inventory
from Item import Item
from ItemType import ItemType
from NPC import NPC
from InventoryUI import InventoryUI
from Settings import *
from ShopInventory2UI import ShopInventory2UI


def can_sell_equipment(equipment, player):
    return player.player_data.coins >= equipment.price


def sell_equipment(equipment, player):
    if can_sell_equipment(equipment, player):
        player.player_data.coins -= equipment.price
        player.player_data.inventory.add_item(Item(equipment.item_type, 1))
        if player.player_data.quest is not None and player.player_data.quest.quest == Quests.CHAMPION:
            player.player_data.quest.specific_cond = True
        return True
    return False


class Shopkeeper(NPC):
    def __init__(self, pos, groups, collision_sprites, current_dialogue, player, timer):
        super().__init__(pos, groups, collision_sprites, current_dialogue, player, timer)
        self.inventory = Inventory()
        self.populate_inventory()
        self.inventoryUI = None

    def populate_inventory(self):
        for item_type in ItemType:
            self.inventory.add_item(Item(item_type))

    def dialogue(self):
        responses, last_dialogue = super().dialogue()
        if len(responses) > 0 and responses[0] == 0:
            self.inventoryUI = ShopInventory2UI(self.groups, self.inventory, self.player, self)


    # def action(self, player):
    #     ShopInventory2UI(self.groups, self.inventory, self.player)
