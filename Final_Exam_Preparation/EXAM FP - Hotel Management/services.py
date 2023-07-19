import random
import unittest
from datetime import date, timedelta, datetime
from texttable import Texttable
from reservationsRepo import ReservationsRepo
from rooms import Room
from reservation import Reservation

class RoomException(Exception):
    pass

class Services:
    def __init__(self, reservationsFile="reservations.txt", rooms="rooms.txt"):
        resRepo = ReservationsRepo(reservationsFile)
        self.__resRepo = resRepo
        self.__resFile = reservationsFile
        self.__roomsFile = rooms
        self.__rooms = []
        self.loadRooms()

    def loadRooms(self):
        with open(self.__roomsFile, "r") as fin:
            for line in fin:
                tokens = line.split(" ")
                try:
                    roomNr = int(tokens[0].strip())
                    type = int(tokens[1].strip())
                except TypeError as te:
                    print(str(te) + "\n There is an error in rooms.txt")

                # if the room is already added we just change the type
                found = False
                for room in self.__rooms:
                    if room.id == roomNr:
                        room.type = type
                        found = True
                        break

                # else if is the first time we add the room
                if not found:
                    newRoom = Room(roomNr, type)
                    self.__rooms.append(newRoom)

    def freeRooms(self, arrivalDate: date, departureDate: date):
        #TODO tests
        """
        Return the number of the rooms free in the given period of time
        :param arrivalDate: date
        :param departureDate: date
        :return: string with the ids of rooms free
        """
        string = ""
        free_rooms = []
        for room in self.__rooms:
            if room.RoomFree(arrivalDate, departureDate) == True:
                string += f"{room.id} - {room.type} persons\n"
                free_rooms.append(room.id)

        if string == "":
            string = "There is no room free in this period! Try another period."

        return string, free_rooms

    def roomByID(self, id):
        for room in self.__rooms:
            if room.id == id:
                return room

        raise RoomException("The room with this id does not exist!")

    def createReservation(self, roomNr, name, nrGuests, arrivalDate: date, departureDate: date):
        self.__rooms[roomNr - 1].reserveRoom(arrivalDate, departureDate)
        self.__resRepo.addReservation(roomNr, name, nrGuests, arrivalDate, departureDate)

    def addReservation(self, roomNr, name, nrGuests, arrivalDate: date, departureDate: date):
        """
        Adding a new reservation
        :param roomNr: room number
        :param name: the name
        :param nrGuests: the number of guests
        :param arrivalDate: arrivalDate
        :param departureDate: departureDate
        :return: nothing
        """
        # TODO tests
        self.__rooms[roomNr - 1].reserveRoom(arrivalDate, departureDate)
        self.__resRepo.addReservation(roomNr, name, nrGuests, arrivalDate, departureDate)

    def saveResFile(self):
       self.__resRepo.saveResFile()

    def generate_1000_Reservations(self):
        # loading the types of the rooms
        self.loadRooms()

        #
        familyName = ["Enache", "Popescu", "Monarh", "Popa", "Thira", "Paveluc", "Dumitrescu", "Dumitrana", "Cheres",
                      "Herta", "Olteanu", "Rusu", "Ungureanu", "Turcu"]
        givenName = ["Vlad", "Ioan", "Maria", "Andreea", "Octavian", "Mara", "Elena", "George", "Samuel", "Vasile",
                     "Stefan", "Paula", "Diana", "Oana", "David", "Dragos", "Maria"]

        # generating 100 names
        names = []
        while len(names) < 100:
            family = random.choice(familyName)
            given = random.choice(givenName)
            name = family + " " + given
            if name not in names:
                names.append(name)

        reservations = []
        # room 1
        while len(self.__resRepo.reservations) < 200:
            name = random.choice(names)
            day = random.randint(0, 365)
            arrivalDate = date(2023, 1, 1) + timedelta(days=day)
            departureDate = arrivalDate + timedelta(random.randint(0, 2))
            if self.__rooms[0].RoomFree(arrivalDate, departureDate) == False:
                continue
            nrGuests = random.randint(1, self.__rooms[0].type)
            self.addReservation(1, name, nrGuests, arrivalDate, departureDate)

        # room 2
        while len(self.__resRepo.reservations) < 400:
            name = random.choice(names)
            day = random.randint(0, 365)
            arrivalDate = date(2023, 1, 1) + timedelta(days=day)
            departureDate = arrivalDate + timedelta(random.randint(0, 2))
            if self.__rooms[1].RoomFree(arrivalDate, departureDate) == False:
                continue
            nrGuests = random.randint(1, self.__rooms[1].type)
            self.addReservation(2, name, nrGuests, arrivalDate, departureDate)

        # room 3
        while len(self.__resRepo.reservations) < 600:
            name = random.choice(names)
            day = random.randint(0, 365)
            arrivalDate = date(2023, 1, 1) + timedelta(days=day)
            departureDate = arrivalDate + timedelta(random.randint(0, 2))
            if self.__rooms[2].RoomFree(arrivalDate, departureDate) == False:
                continue
            nrGuests = random.randint(1, self.__rooms[2].type)
            self.addReservation(3, name, nrGuests, arrivalDate, departureDate)

        # room 4
        while len(self.__resRepo.reservations) < 800:
            name = random.choice(names)
            day = random.randint(0, 365)
            arrivalDate = date(2023, 1, 1) + timedelta(days=day)
            departureDate = arrivalDate + timedelta(random.randint(0, 2))
            if self.__rooms[3].RoomFree(arrivalDate, departureDate) == False:
                continue
            nrGuests = random.randint(1, self.__rooms[3].type)
            self.addReservation(4, name, nrGuests, arrivalDate, departureDate)

        # room 5
        while len(self.__resRepo.reservations) < 1000:
            name = random.choice(names)
            day = random.randint(0, 365)
            arrivalDate = date(2023, 1, 1) + timedelta(days=day)
            departureDate = arrivalDate + timedelta(random.randint(0, 2))
            if self.__rooms[4].RoomFree(arrivalDate, departureDate) == False:
                continue
            nrGuests = random.randint(1, self.__rooms[4].type)
            self.addReservation(5, name, nrGuests, arrivalDate, departureDate)

        # saving the generated reservations to file
        self.__resRepo.saveResFile()

    def loadReservations(self):
        # there is a problem when loading id from the file - I do not know how bad is it
        with open(self.__resFile, "r") as fin:
            for line in fin:
                tokens = line.split(",")
                id = int(tokens[0].strip())
                roomNr = int(tokens[1].strip())
                name = tokens[2].strip()
                nrGuests = int(tokens[3].strip())
                arrivalDate = datetime.strptime(tokens[4].strip(), "%Y-%m-%d").date()
                departureDate = datetime.strptime(tokens[5].strip(), "%Y-%m-%d").date()
                newRes = Reservation(id, roomNr, name, nrGuests, arrivalDate, departureDate)
                self.__rooms[roomNr - 1].reserveRoom(arrivalDate, departureDate)
                self.__resRepo.addReservation(roomNr, name, nrGuests, arrivalDate, departureDate)

    def displayRes(self, startDate: date, endDate: date):
        resDisplay = []
        for res in self.__resRepo.reservations:
            if (res.arrivalDate > startDate and res.arrivalDate < endDate) or (res.departureDate > startDate and res.departureDate < endDate):
                resDisplay.append(res)


        for i in range(len(resDisplay) - 1):
            for j in range(i + 1, len(resDisplay)):
                if resDisplay[i].arrivalDate > resDisplay[j].arrivalDate:
                    resDisplay[i], resDisplay[j] = resDisplay[j], resDisplay[i]

        if len(resDisplay) == 0:
            return "There are no reservations in the given interval."
        firstMonth = resDisplay[0].arrivalDate.month
        lastMonth = resDisplay[-1].arrivalDate.month
        Month = firstMonth
        MonthDate = date(2023, Month, 1)
        index = 0   # used for going through resDisplay
        string = "This reservations where deleted:\n"
        while Month <= lastMonth:
            table = Texttable()
            table.header([MonthDate.strftime("%B"), "Name", "Guests"])

            while index < len(resDisplay) and resDisplay[index].arrivalDate.month == Month:
                table.add_row([f"{resDisplay[index].arrivalDate.strftime('%m.%d')} - {resDisplay[index].departureDate.strftime('%m.%d')}", str(resDisplay[index].name), f"{resDisplay[index].nrGuests} person(s)"])
                index += 1

            string += table.draw() + "\n\n"

            Month += 1
            MonthDate = date(2023, Month, 1)

        return string

    def deleteResByID(self, idRes):
        for res in self.__resRepo.reservations:
            if res.id == idRes:
                # making the room unused on that period
                self.__rooms[res.roomNr - 1].deleteRes(res.arrivalDate, res.departureDate)
                # deleting the reservation from the reservation list
                deletedRes = res
                self.__resRepo.reservations.remove(res)
                self.__resRepo.saveResFile()
                return f"The reservation {deletedRes} was deleted succesfully."
        return f"The reservation with id {idRes} does not exists."

    def deleteIntervalRoom(self, roomNr: int, startDate: date, endDate: date):
        resDisplay = []

        # searching and deleting all reservations on that room in that period
        for res in self.__resRepo.reservations:
            if res.roomNr == roomNr and ((res.arrivalDate > startDate and res.arrivalDate < endDate) or (res.departureDate > startDate and res.departureDate < endDate)):
                # making the room unused on that period
                self.__rooms[res.roomNr - 1].deleteRes(res.arrivalDate, res.departureDate)
                resDisplay.append(res)
                self.__resRepo.reservations.remove(res)
                self.__resRepo.saveResFile()

        if len(resDisplay) == 0:
            return f"There are no reservations in the given interval for room {roomNr}."

        firstMonth = resDisplay[0].arrivalDate.month
        lastMonth = resDisplay[-1].arrivalDate.month
        Month = firstMonth
        MonthDate = date(2023, Month, 1)
        index = 0  # used for going through resDisplay
        string = ""
        while Month <= lastMonth:
            table = Texttable()
            table.header([MonthDate.strftime("%B"), "Name", "Guests"])

            while index < len(resDisplay) and resDisplay[index].arrivalDate.month == Month:
                table.add_row([
                                  f"{resDisplay[index].arrivalDate.strftime('%m.%d')} - {resDisplay[index].departureDate.strftime('%m.%d')}",
                                  str(resDisplay[index].name), f"{resDisplay[index].nrGuests} person(s)"])
                index += 1

            string += table.draw() + "\n\n"

            Month += 1
            MonthDate = date(2023, Month, 1)

        return string

    def monthlyReport(self, month: int):
        table = Texttable()
        table.header(["M", "T", "W", "T", "F", "S", "S"])
        firstDay = date(2023, month, 1)
        lastDay = date(2023, month + 1, 1)
        Day = firstDay
        row = []
        while len(row) < Day.weekday():
            row.append(" ")
        while Day < lastDay:
            string, freeRooms = self.freeRooms(Day, Day + timedelta(days=1))
            if len(row) == 7:
                table.add_row(row)
                row = []
            row.append(f"{Day.day}/{len(freeRooms)}")
            Day = Day + timedelta(days=1)

        while len(row) < 7:
            row.append(" ")

        table.add_row(row)

        return table.draw()

class CreateReservationTests(unittest.TestCase): # TODO
    def setUp(self) -> None:
        resRepo = Services("resRepoTest.txt", "roomsTest.txt")

if __name__ == "__main__":
    service = Services()
    service.loadReservations()
    print("Yess")
    print(service.displayRes(date(2023, 2, 1), date(2023, 2, 15)))
