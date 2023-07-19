from src.repository import TaxiRepo


class Services:
    def __init__(self):
        self.repo = TaxiRepo()

    def generateNTaxis(self, n):
        self.repo.generateNTaxis(n)

    def closestTaxi(self, x, y):
        """
        This function find the closest taxi to the position (x, y)
        :param x: x coordonate
        :param y: y coordonate
        :return: id taxi
        """
        return self.repo.closestTaxi(x, y)

    def addFare(self, id, fare):
        """
        This function add a fare to an taxi
        :param id: id of taxi
        :param fare: the fare to add
        :return: nothing
        """
        self.repo.addFare(id, fare)

    def display_all_taxis(self):
        """
        This function displays all taxis in descending order of their fare
        :return: a string
        """
        return str(self.repo)

    def placeTaxi(self,id, x, y):
        self.repo.placeTaxi(id, x, y)