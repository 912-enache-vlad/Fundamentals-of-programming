from datetime import date, timedelta


class Room:
    def __init__(self, id: int, type: int):
        self.__id = id
        self.__type = type
        self.__used = []

    @property
    def id(self):
        return self.__id

    @property
    def used(self):
        return self.__used

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, newType: int):
        self.__type = newType
    
    def deleteRes(self, arrivalDate: date, departureDate: date):
        arrival = arrivalDate
        difference = departureDate - arrivalDate
        for i in range(difference.days):
            day = arrival + timedelta(days=i)
            if day in self.__used:
                self.__used.remove(day)
    
    def reserveRoom(self, arrivalDate: date, departureDate: date):
        arrival = arrivalDate
        difference = departureDate - arrivalDate
        for i in range(difference.days):
            day = arrival + timedelta(days=i)
            self.__used.append(day)

    def RoomFree(self, startDate: date, endDate: date):
        """
        Return True if the room is used in at least one day of the given interval or False otherwise
        """
        start = startDate
        diff = endDate - startDate
        for i in range(diff.days):
            day = start + timedelta(days= i)
            if day in self.__used:
                return False

        return True

if __name__ == "__main__":
    room1 = Room(1, 4)
    room1.reserveRoom(date(2023, 5, 10), date(2023, 5, 20))
    print(room1.RoomFree(date(2023, 5, 9), date(2023, 5, 11)))

