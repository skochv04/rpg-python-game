from enum import Enum

from Item import Item
from ItemType import ItemType
from Settings import *


class Quests(Enum):
    # id, name, level, prizeCoins, prizeHealth, prizeEquipment[], prizeSkills[], toNextLevel (?)
    # enemiesToWin, coinsToCollect, itemsToBuy, specific_cond (?)

    # specific_cond - for example, try Fortune, then FortuneNPC will write down that you have done this task
    FIRST_STEPS = (1, "First steps", 1, 40, 0, [], [], False, 0, 10, [Item(ItemType.ACID, 1)], False)
