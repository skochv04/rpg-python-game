from Inventory import Inventory
from Item import Item
from ItemType import ItemType
from NPC import NPC
from Settings import *
# from ShopkeeperInventory import ShopkeeperInventoryUI

def sell_equipment(equipment, player):
    if player.money >= equipment.price:
        player.money -= equipment.price
        player.equipment += [equipment]
        return True
    return False

class Shopkeeper(NPC):
    def __init__(self, pos, groups, collision_sprites, current_dialogue, player, timer):
        super().__init__(pos, groups, collision_sprites, current_dialogue, player, timer)
        self.inventory = Inventory()
        self.populate_inventory()
        # self.shop_ui = ShopkeeperInventoryUI(player, self.inventory)

    def populate_inventory(self):
        for item_type in ItemType:
            self.inventory.add_item(Item(item_type, 10))

    def action(self, player):
        pass
        # self.shop_ui.run()