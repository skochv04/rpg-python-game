class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: " + self.x + ", y: " + self.y;

    def precedes(self, vector):
        return self.x <= vector.x and self.y <= vector.y

    def follows(self, vector):
        return self.x >= vector.x and self.y >= vector.y

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def subtract(self, vector):
        self.x -= vector.x
        self.y -= vector.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))