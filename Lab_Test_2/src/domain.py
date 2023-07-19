

class Taxi:
    def __init__(self, id, x, y, fare):
        self.id = id
        self.x = x
        self.y = y
        self.fare = 0

    def __str__(self):
        return f"{self.id}, ({self.x}, {self.y}), fare = {self.fare}"