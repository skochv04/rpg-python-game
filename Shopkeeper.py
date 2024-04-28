from NPC import NPC


def sell_equipment(equipment, player):
    if player.money >= equipment.price:
        player.money -= equipment.price
        player.equipment += [equipment]
        return True
    return False


class Shopkeeper(NPC):
    def action(self, player):
        raise NotImplementedError
