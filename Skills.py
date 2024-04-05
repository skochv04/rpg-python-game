from enum import Enum


class SKILLS(Enum):
    SKILL1 = ('a', 20, 1)
    SKILL2 = ('b', 15, 2)
    SKILL3 = ('c', 20, 3)
    SKILL4 = ('d', 25, 4)
    SKILL5 = ('e', 45, 5)
    SKILL6 = ('f', 50, 6)
    SKILL7 = ('g', 10, 7)
    SKILL8 = ('h', 40, 8)

    def __str__(self):
        return self.value[0]
