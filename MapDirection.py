from enum import Enum
from Vector2D import Vector2D


class MapDirection(Enum):
    LEFT_1 = ('<', Vector2D(-1, 0), 1)
    LEFT_2 = ('(<)', Vector2D(-1, 0), 2)
    RIGHT_1 = ('>', Vector2D(1, 0), 3)
    RIGHT_2 = ('(>)', Vector2D(1, 0), 4)
    TOP_1 = ('^', Vector2D(0, 1), 5)
    TOP_2 = ('(^)', Vector2D(0, 1), 6)
    DOWN_1 = ('v', Vector2D(0, -1), 7)
    DOWN_2 = ('(v)', Vector2D(0, -1), 8)

    def __str__(self):
        return self.value[0]
