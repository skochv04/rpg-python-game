from enum import Enum

from Skills import Skills
from Item import Item
from ItemType import ItemType
from Settings import *


class Quests(Enum):
    # id, name, level, prizeExp, prizeCoins, prizeHealth, prizeEquipment[], prizeSkills[], toNextLevel (?)
    # enemiesToWin, coinsToEarn, itemsToBuy, specific_cond (?)

    # specific_cond - for example, try Fortune, then FortuneNPC will write down that you have done this task
    FIRST_STEPS = (1, "First steps", 1, 10, 30, 0, [], [], False, 0, 10, [Item(ItemType.THREAD, 1)], False, "Buy 1 thread and earn 10 coins")
    MAGIC_DUEL = (2, "Magic duel", 1, 15, 50, 0, [Item(ItemType.ACID, 1)], [], False, 1, 0, [], True, "Try your fortune and win in one duel")
    CHAMPION = (3, "Champion", 1, 20, 60, 100, [], [], True, 2, 0, [], True, "Buy any equipment and win all magic enemies")
