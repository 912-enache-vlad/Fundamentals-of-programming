from random import randint

from src.services import Services


class UI:
    def __init__(self):
        self.services = Services()

    def __call__(self):
        print("N between 0 and 10")
        n = int(input("Number of operational taxis: "))
        self.services.generateNTaxis(n)

        while True:
            choice = input("""
            1 - Add a Ride
            2 - Simulate a Ride 
            """)

            if choice == "1":
                try:
                    startX = int(input("Start x: "))
                    startY = int(input("Start y: "))
                    endX = int(input("End x: "))
                    endY = int(input("End y: "))

                    if startX < 0 or startY < 0 or startY > 100 or startX > 100:
                        raise ValueError("x and y should be between 0 and 100!")
                    if endX < 0 or endY < 0 or endY > 100 or endX > 100:
                        raise ValueError("x and y should be between 0 and 100!")

                    idClosest = self.services.closestTaxi(startX, startY)

                    fare = abs(startX - endX) + abs(startY - endY)
                    self.services.placeTaxi(idClosest, endX, endY)
                    self.services.addFare(idClosest, fare)
                    print(self.services.display_all_taxis())
                except ValueError as ve:
                    print(ve)

            elif choice == "2":

                startX = randint(0, 100)
                startY = randint(0, 100)
                endX = randint(0, 100)
                endY = randint(0, 100)
                while abs(endX - startX) + abs(endY - startY) < 10:
                    startX = randint(0, 100)
                    startY = randint(0, 100)
                    endX = randint(0, 100)
                    endY = randint(0, 100)


                idClosest = self.services.closestTaxi(startX, startY)

                fare = abs(startX - endX) + abs(startY - endY)
                self.services.placeTaxi(idClosest, endX, endY)
                self.services.addFare(idClosest, fare)
                print(self.services.display_all_taxis())


