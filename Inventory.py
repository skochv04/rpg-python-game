from Settings import *
from Item import Item

class Inventory:
    def __init__(self):
        self.rows = 5
        self.columns = 4
        self.inventory = [[0 for _ in range(self.rows)] for _ in range(self.columns)]

    def add_item(self, item):
        for i in range(self.columns):
            for j in range(self.rows):
                if self.inventory[i][j] == 0:
                    self.inventory[i][j] = item
                    return True
        return False

    def remove_item(self, item):
        for i in range(self.columns):
            for j in range(self.rows):
                if self.inventory[i][j] == item:
                    result = self.inventory[i][j].decrease_amount()
                    if self.inventory[i][j].amount == 0:
                        self.inventory[i][j] = 0
                    return result

        return False


    def get_item(self, i, j):
        return self.inventory[i][j]

    def get_inventory(self):
        return self.inventory

    def get_inventory_size(self):
        return len(self.inventory)

    def item_move(self, i, j, x, y):
        if self.inventory[x][y] == 0:
            self.inventory[x][y] = self.inventory[i][j]
            self.inventory[i][j] = 0
        else:
            self.inventory[x][y], self.inventory[i][j]  = self.inventory[i][j], self.inventory[x][y]

        return True