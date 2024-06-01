from enum import Enum

from Item import Item
from ItemType import ItemType
from Settings import *


class Quests(Enum):
    # id, name, level, prizeExp, prizeCoins, prizeHealth, prizeEquipment[], prizeSkills[], toNextLevel (?)
    # enemiesToWin, coinsToCollect, itemsToBuy, specific_cond (?)

    # specific_cond - for example, try Fortune, then FortuneNPC will write down that you have done this task
    FIRST_STEPS = (1, "First steps", 1, 10, 30, 0, [], [], False, 0, 0, [Item(ItemType.THREAD, 1)], False)
    MAGIC_DUEL = (2, "Magic duel", 1, 15, 50, 0, [Item(ItemType.ACID, 1)], [], False, 0, 0, [], True)
