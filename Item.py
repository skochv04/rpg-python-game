class Item:
    def __init__(self, item_type, amount):
        self.name = item_type.name
        self.id = item_type.value[0]
        self.description = f"Price: {item_type.value[1]}, Damage: {item_type.value[2]}, Min Power: {item_type.value[3]}"
        self.value = item_type.value[1]
        self.image = item_type.value[4]
        self.amount = amount
        self.x = None
        self.y = None
        self.item_type = item_type

    def decrease_amount(self):
        if self.amount > 0:
            self.amount -= 1
            return True
        return False

    def increase_amount(self, amount = 1):
        self.amount += amount
        return True

    def __str__(self):
        return self.name
