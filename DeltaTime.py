from Settings import *

class DT:
    def __init__(self, clock):
        self.clock = clock
        self.__dt = 0

    def update(self):
        self.__dt = self.clock.tick() / 1000

    def set(self, val):
        self.update()
        self.__dt = val

    def get(self):
        return self.__dt


# dt = DT(pygame.time.Clock())
# while True:
#     dt.update()
#     print(dt.get())
#     pygame.time.wait(140)
#     dt.update()