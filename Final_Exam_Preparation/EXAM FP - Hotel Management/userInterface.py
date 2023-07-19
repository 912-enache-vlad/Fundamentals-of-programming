from datetime import date, datetime

from services import Services


class UserInterface:
    def __init__(self, service: Services):
        self.__service = service

    def __call__(self):
        while True:
            choice = input("""
            1 - use the existent reservations from the file
            2 - generate new 1000 reservations 
            """)
            if choice == "2":
                self.__service.generate_1000_Reservations()
                break

            elif choice == "1":
                self.__service.loadReservations()
                break
            else:
                print("Invalid command!")

        while True:
            choice = input("""
            1 - display all reservations from an interval
            2 - create new reservation
            3 - delete reservation(s)
            4 - monthly report
            """)
            if choice == "1":
                arrival = input("Arival Date(%d.%m): ")
                arrivalDate = datetime.strptime(arrival, "%d.%m").date()
                arrivalDate = date(2023, arrivalDate.month, arrivalDate.day)
                departure = input("Departure Date(%d.%m): ")
                departureDate = datetime.strptime(departure, "%d.%m").date()
                departureDate = date(2023, departureDate.month, departureDate.day)
                print(self.__service.displayRes(arrivalDate, departureDate))

            elif choice == "2":     #TODO tests and specifications for functions used for this functionality
                arrival = input("Arival Date(%d.%m): ")
                arrivalDate = datetime.strptime(arrival, "%d.%m").date()
                arrivalDate = date(2023, arrivalDate.month, arrivalDate.day)
                departure = input("Departure Date(%d.%m): ")
                departureDate = datetime.strptime(departure, "%d.%m").date()
                departureDate = date(2023, departureDate.month, departureDate.day)
                strFreeRooms, free_rooms = self.__service.freeRooms(arrivalDate, departureDate)

                roomNr = int(input(strFreeRooms + "\n>>>"))
                if roomNr not in free_rooms:
                    print("You have not chosen from the free rooms. Please try again.")
                    continue

                name = input("Name: ")
                if name == "":
                    print("The name is empty, please try again.")
                    continue

                nrGuests = int(input("Number of Guests: "))
                if nrGuests > self.__service.roomByID(roomNr).type:
                    print("The number of guests is too high for this room.")
                    continue

                cancel = input("If you want to cancel enter 'y'.")
                if cancel.lower() == "y":
                    print("You canceled your reservation.")
                    continue

                self.__service.createReservation(roomNr, name, nrGuests, arrivalDate, departureDate)

            elif choice == "3":
                choice2 = input("""
                1 - delete a reservation by its ID
                2 - delete reservations from an interval for a room 
                """)
                if choice2 == "1":
                    id = int(input("Id: "))
                    print(self.__service.deleteResByID(id))

                elif choice2 == "2":
                    try:
                        arrival = input("Arival Date(%d.%m): ")
                        arrivalDate = datetime.strptime(arrival, "%d.%m").date()
                        arrivalDate = date(2023, arrivalDate.month, arrivalDate.day)
                        departure = input("Departure Date(%d.%m): ")
                        departureDate = datetime.strptime(departure, "%d.%m").date()
                        departureDate = date(2023, departureDate.month, departureDate.day)
                        roomNr = int(input("Room number: "))
                        print(self.__service.deleteIntervalRoom(roomNr, arrivalDate, departureDate))
                    except Exception as e:
                        print(e)
                else:
                    print("Invalid command. Please try again.")
            elif choice == "4":
                month = int(input("Month (1 - 12):"))
                print(self.__service.monthlyReport(month))
            else:
                print("Invalid command!")

