from Settings import *
from InventoryUI import InventoryUI


class GeneralUI:
    def __init__(self, groups, player_data, player):
        self.player_data = player_data
        self.player = player
        self.groups = groups

        self.inventory = None
        self.last_input = pygame.time.get_ticks()

    def create_inventory(self):
        self.inventory = InventoryUI(self.groups, self.player.player_data.inventory, self.player)

    def input(self):
        keys = pygame.key.get_pressed()
        if pygame.time.get_ticks() - self.last_input < 190:
            return
        if keys[pygame.K_i] and self.inventory is None:
            self.create_inventory()
        elif keys[pygame.K_i] and self.inventory is not None:
            self.inventory.kill()
            self.inventory = None

        self.last_input = pygame.time.get_ticks()

    def update(self, dt):
        self.input()
        if self.inventory is not None:
            self.inventory.update(dt)
