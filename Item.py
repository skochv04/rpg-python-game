
class Item:
    def __init__(self, name, id_number, description, value, image, amount, usable_during_battle = False):
        self.name = name
        self.id = id_number
        self.description = description
        self.value = value
        self.image = image
        self.amount = amount
        self.usable_during_battle = usable_during_battle
        self.x = None
        self.y = None

    def descrease_amount(self):
        if self.amount > 0:
            self.amount -= 1
            return True
        return False

    def increase_amount(self):
        self.amount += 1
        return True

    def __str__(self):
        return self.name