
class Item:
    def __init__(self, name, id_number, description, value, image, amount):
        self.name = name
        self.id = id_number
        self.description = description
        self.value = value
        self.image = image
        self.amount = amount
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