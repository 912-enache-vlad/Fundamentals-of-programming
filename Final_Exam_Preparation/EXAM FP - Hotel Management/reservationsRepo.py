import random
from datetime import date, timedelta, datetime
from rooms import Room
from reservation import Reservation

class ReservationError(Exception):
    pass

class ReservationsRepo:
    def __init__(self, reservationsFile="reservations.txt"):
        self.__reservations = []
        self.__resId = 1
        self.__resFile = reservationsFile

    @property
    def reservations(self):
        return self.__reservations

    def createReservation(self, roomNr, name, nrGuests, arrivalDate: date, departureDate: date):
        newRes = Reservation(self.__resId, roomNr, name, nrGuests, arrivalDate, departureDate)
        self.__resId += 1
        self.__reservations.append(newRes)
        self.appendResFile(newRes)      # appending to the file

    def addReservation(self, roomNr, name, nrGuests, arrivalDate: date, departureDate: date):
        # TODO verifications


        newRes = Reservation(self.__resId, roomNr, name, nrGuests, arrivalDate, departureDate)
        self.__resId += 1
        self.__reservations.append(newRes)

    def saveResFile(self):
        with open(self.__resFile, "w") as fout:
            for res in self.__reservations:
                fout.write(str(res) + "\n")

    def appendResFile(self, res: Reservation):  #TODO tests
        with open(self.__resFile, "a") as fap:
            fap.write(str(res) + "\n")





if __name__ == "__main__":
    resRepo = ReservationsRepo()
    resRepo.loadReservations()
    resRepo.saveResFile()
