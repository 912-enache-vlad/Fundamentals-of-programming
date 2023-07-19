import unittest

from src.domain import Taxi
from src.repository import TaxiRepo
from src.services import Services


class addRideTest(unittest.TestCase):
    def testAddRide(self):
        repo = TaxiRepo()
        taxi1 = Taxi(1, 10, 10, 0)
        repo.taxis.append(taxi1)
        taxi2 = Taxi(2, 50, 50, 0)
        repo.taxis.append(taxi2)
        startX, startY = 11, 11
        endX, endY = 20, 20
        idClosest = repo.closestTaxi(11, 11)
        fare = abs(startX - endX) + abs(startY - endY)
        repo.placeTaxi(idClosest, endX, endY)
        repo.addFare(idClosest, fare)
        self.assertEqual(idClosest, 1)
        self.assertEqual(fare, 18)
        for taxi in repo.taxis:
            if taxi.id == idClosest:
                self.assertEqual(taxi.x, endX)
                self.assertEqual(taxi.y, endY)

