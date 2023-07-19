from random import randint

from src.domain import Taxi


class TaxiRepo:
    def __init__(self):
        self.taxis = []

    def generateNTaxis(self, n):
        idCount = 1
        x = randint(0, 100)
        y = randint(0, 100)
        taxi = Taxi(idCount, x, y, 0)
        self.taxis.append(taxi)
        idCount += 1

        while idCount <= n:
            x = randint(0, 100)
            y = randint(0, 100)

            for taxi in self.taxis:
                if abs(taxi.x - x) + abs(taxi.y - y) <= 5:
                    continue #if distance < 6 continue

            taxi = Taxi(idCount, x, y, 0)
            self.taxis.append(taxi)
            idCount += 1

    def closestTaxi(self, x, y):
        """
        This function find the closest taxi to the position (x, y)
        :param x: x coordonate
        :param y: y coordonate
        :return: id taxi
        """
        idClosest = -1
        closestDist = 100000
        for taxi in self.taxis:
            if abs(taxi.x - x) + abs(taxi.y - y) < closestDist:
                closestDist = abs(taxi.x - x) + abs(taxi.y - y)
                idClosest = taxi.id

        return idClosest

    def addFare(self, id, fare):
        """
        This function add a fare to an taxi
        :param id: id of taxi
        :param fare: the fare to add
        :return: nothing
        """

        for taxi in self.taxis:
            if taxi.id == id:
                taxi.fare += fare

    def placeTaxi(self, id, x, y):
        for taxi in self.taxis:
            if taxi.id == id:
                taxi.x = x
                taxi.y = y
                break

    def __str__(self):
        """
        This function displays all taxis in descending order of their fare
        :return: a string
        """
        #sorting
        for i in range(len(self.taxis) - 1):
            for j in range(i, len(self.taxis)):
                if self.taxis[i].fare < self.taxis[j].fare:
                    self.taxis[i], self.taxis[j] = self.taxis[j], self.taxis[i]


        string = ""
        for taxi in self.taxis:
            string += str(taxi) + "\n"

        return string