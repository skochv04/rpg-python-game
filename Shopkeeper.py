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
        print(player.player_data.coins, equipment.price)
        player.player_data.coins -= equipment.price
        player.player_data.inventory.add_item(Item(equipment.item_type, 1))
        return True
    return False


class Shopkeeper(NPC):
    def __init__(self, pos, groups, collision_sprites, current_dialogue, player, timer):
        super().__init__(pos, groups, collision_sprites, current_dialogue, player, timer)
        self.inventory = Inventory()
        self.populate_inventory()

    def populate_inventory(self):
        for item_type in ItemType:
            self.inventory.add_item(Item(item_type))

    def dialogue(self):
        responses = super().dialogue()
        if responses[0] == 0:
            ShopInventory2UI(self.groups, self.inventory, self.player)

    def action(self, player):
        ShopInventory2UI(self.groups, self.inventory, self.player)
