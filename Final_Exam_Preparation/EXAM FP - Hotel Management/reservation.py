import datetime


class Reservation:
    def __init__(self, id: int, roomNr: int, name: str, nrGuests: int, arrivalDate: datetime.date, departureDate: datetime.date):
        self.__id = id
        self.roomNr = roomNr
        self.name = name
        self.nrGuests = nrGuests
        self.arrivalDate = arrivalDate
        self.departureDate = departureDate

    @property
    def id(self):
        return self.__id

    def  __str__(self):
        return f"{self.__id}, {self.roomNr}, {self.name}, {self.nrGuests}, {self.arrivalDate}, {self.departureDate}"