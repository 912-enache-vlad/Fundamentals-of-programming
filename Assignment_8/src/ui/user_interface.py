from datetime import datetime

from src.domain.activity import Activity
from src.domain.person import Person
from src.repository.activityRepo import ActivityRepo, ActivityRepoException
from src.repository.personRepo import PersonRepo, PersonRepoException
from src.services.services import Services


def validate_date(date:str):
    date_format = "%d.%m.%Y"
    try:
        datetime.strptime(date, date_format)
    except ValueError:
        raise ValueError("Incorrect data format, it should be ~DD.MM.YYYY~")


def validate_time(time:str):
    time_format = "%H:%M"
    times = time.split("-")
    start_time = times[0].strip()
    end_time = times[1].strip()
    try:
        datetime.strptime(start_time, time_format)
        datetime.strptime(end_time, time_format)
    except ValueError:
        raise ValueError("Incorrect time format, it should be ~HH:MM - HH:MM~")
    
    
class User_Interface:

    def __init__(self, services: Services):
        self.__services = services

    def __call__(self):
        # having 20 procedurally generated persons
        if True:
            self.__services.add_person('1', "Vlad", "0741234567")
            self.__services.add_person('2', "Mara", "0788465978")
            self.__services.add_person('3', "Alex", "0724567890")
            self.__services.add_person('4', "Andrei", "0741556789")
            self.__services.add_person('5', "Mihai", "0784567890")
            self.__services.add_person('6', "Ion", "0724567891")
            self.__services.add_person('7', "Maria", "0744567892")
            self.__services.add_person('8', "Ana", "0784567893")
            self.__services.add_person('9', "Ioana", "0724567894")
            self.__services.add_person('10', "Vasile", "0744567895")
            self.__services.add_person('11', "Gheorghe", "0784567896")
            self.__services.add_person('12', "Diana", "0724567897")
            self.__services.add_person('13', "Cristina", "0744567898")
            self.__services.add_person('14', "Catalin", "0784567899")
            self.__services.add_person('15', "Ciprian", "0724567800")
            self.__services.add_person('16', "Marian", "0744567801")
            self.__services.add_person('17', "Mihail", "0784567802")
            self.__services.add_person('18', "Mihai", "0724567803")
            self.__services.add_person('19', "George", "0744567804")
            self.__services.add_person('20', "John", "0784567805")

        # # having 20 procedurally generated activities
        if True:
            self.__services.add_activity('1', ['1', '2', '3', '4', '5'], "12.12.2022", "12:00 - 13:00", "Basketball")
            self.__services.add_activity('5', ['1', '2', '3', '4', '5'], "12.12.2022", "16:00 - 17:00", "Basketball")
            self.__services.add_activity('6', ['6', '7', '8', '9', '10'], "16.01.2023", "17:00 - 18:00", "Football")
            self.__services.add_activity('2', ['6', '7', '8', '9', '10'], "19.12.2022", "13:00 - 14:00", "Football")
            self.__services.add_activity('3', ['11', '12', '13', '14', '15'], "26.12.2022", "14:00 - 15:00", "Volleyball")
            self.__services.add_activity('11', ['11', '12', '13', '14', '15'], "20.02.2023", "22:00 - 23:00", "Volleyball")
            self.__services.add_activity('4', ['16', '17', '18', '19', '20'], "02.01.2023", "15:00 - 16:00", "Tennis")
            self.__services.add_activity('8', ['16', '17', '18', '19', '20'], "30.01.2023", "19:00 - 20:00", "Tennis")
            self.__services.add_activity('7', ['11', '12', '13', '14', '15'], "23.01.2023", "18:00 - 19:00", "Fitness")
            self.__services.add_activity('9', ['1', '2', '3', '4', '5'], "06.02.2023", "20:00 - 21:00", "Gymnastics")
            self.__services.add_activity('10', ['6', '7', '8', '9', '10'], "13.02.2023", "21:00 - 22:00", "Golf")
            self.__services.add_activity('12', ['16', '17', '18', '19', '20'], "27.02.2023", "23:00 - 00:00", "Swimming")
            self.__services.add_activity('13', ['11', '12', '13', '14', '15'], "06.03.2023", "00:00 - 01:00", "Running")
            self.__services.add_activity('14', ['1', '2', '3', '4', '5'], "13.03.2023", "01:00 - 02:00", "Cycling")
            self.__services.add_activity('15', ['6', '7', '8', '9', '10'], "20.03.2023", "02:00 - 03:00", "Yoga")
            self.__services.add_activity('16', ['16', '17', '18', '19', '20'], "27.03.2023", "03:00 - 04:00", "Boxing")
            self.__services.add_activity('17', ['11', '12', '13', '14', '15'], "03.04.2023", "04:00 - 05:00", "Hiking")
            self.__services.add_activity('18', ['1', '2', '3', '4', '5'], "10.04.2023", "05:00 - 06:00", "Skiing")
            self.__services.add_activity('19', ['6', '7', '8', '9', '10'], "17.04.2023", "06:00 - 07:00", "Soccer")
            self.__services.add_activity('20', ['16', '17', '18', '19', '20'], "24.04.2023", "07:00 - 08:00", "Dancing")


        while True:
            print("""
            * Manage persons and activities:
            1 - Add a new person
            2 - Remove a person
            3 - Update a person
            4 - List all persons
            5 - Add a new activity
            6 - Remove an activity
            7 - Update an activity
            8 - List all activities
            * Search:
            9 - Search for activities
            10 - Search for persons
            * Statistics:
            11 - Activities for a given date
            12 - Busiest days
            13 - Activities with a given person
            0 - Exit
            """)
            user_command = input(">>>")

            if user_command == "1":
                person_id = input("Person ID: ")
                name = input("Person name: ")
                phone_number = input("Person phone number: ")
                try:
                    self.__services.add_person(person_id, name, phone_number)
                except PersonRepoException as ve:
                    print(f"\n{ve}\n")

            elif user_command == "2":
                person_id = input("Person ID: ")
                try:
                    self.__services.remove_person(person_id)
                except PersonRepoException as ve:
                    print(f"\n{ve}\n")

            elif user_command == "3":
                person_id = input("Person ID: ")
                name = input("Person name: ")
                phone_number = input("Person phone number: ")
                try:
                    self.__services.update_person(person_id, name, phone_number)
                except PersonRepoException as ve:
                    print(f"\n{ve}\n")

            elif user_command == "4":
                print(self.__services.list_all_persons())

            elif user_command == "5":
                activity_id = input("Activity ID: ")

                try:
                    number_of_persons = int(input("Number of persons: "))
                except ValueError:
                    print("\nInvalid number of persons!\n")
                    continue

                persons_id = []
                for i in range(number_of_persons):
                    persons_id.append(input("Person ID: "))

                date = input("Date with exactly this format ~DD.MM.YYYY~: ")
                try:
                    validate_date(date)
                except ValueError as ve:
                    print(f"\n{ve}\n")
                    continue

                time = input("Time with exactly this format ~HH:MM - HH:MM~: ")
                try:
                    validate_time(time)
                except ValueError as ve:
                    print(f"\n{ve}\n")
                    continue
                description = input("Description: ")
                try:
                    self.__services.add_activity(activity_id, persons_id, date, time, description)
                except ActivityRepoException as ve:
                    print(f"\n{ve}\n")
                except PersonRepoException as ve:
                    print(f"\n{ve}\n")

            elif user_command == "6":
                activity_id = input("Activity ID: ")
                try:
                    self.__services.remove_activity(activity_id)
                except ActivityRepoException as ve:
                    print(f"\n{ve}\n")

            elif user_command == "7":
                activity_id = input("Activity ID: ")
                try:
                    number_of_persons = int(input("Number of persons: "))
                except ValueError:
                    print("\nInvalid number of persons!\n")
                    continue
                persons_id = []
                for i in range(number_of_persons):
                    persons_id.append(input("Person ID: "))
                date = input("Date with exactly this format ~DD.MM.YYYY~: ")
                try:
                    validate_date(date)
                except ValueError as ve:
                    print(f"\n{ve}\n")
                    continue
                time = input("Time with exactly this format ~HH:MM - HH:MM~: ")
                try:
                    validate_time(time)
                except ValueError as ve:
                    print(f"\n{ve}\n")
                    continue

                description = input("Description: ")
                try:
                    self.__services.update_activity(activity_id, persons_id, date, time, description)
                except ActivityRepoException as ve:
                    print(f"\n{ve}\n")

            elif user_command == "8":
                print(self.__services.list_all_activities())

            elif user_command == "9":
                print("""
                1 - Search for activities by date
                2 - Search for activities by time
                3 - Search for activities by description
                """)
                user_command = input(">>>")
                if user_command == "1":
                    date = input("Date with exactly this format ~DD.MM.YYYY~: ")
                    try:
                        validate_date(date)
                    except ValueError as ve:
                        print(f"\n{ve}\n")
                        continue
                    result = self.__services.search_activities_by_date(date)
                    if result == "":
                        print("No activities with this date found!")
                    else:
                        print(result)

                elif user_command == "2":
                    time = input("Time with exactly this format ~HH:MM - HH:MM~: ")
                    try:
                        validate_time(time)
                    except ValueError as ve:
                        print(f"\n{ve}\n")
                        continue
                    result = self.__services.search_activities_by_time(time)
                    if result == "":
                        print("No activities with this time found!")
                    else:
                        print(result)

                elif user_command == "3":
                    description = input("Description: ")
                    result = self.__services.search_activities_by_description(description)
                    if result == "":
                        print("No activities with this description found!")
                    else:
                        print(result)

                else:
                    print("Invalid command. Please try again.")

            elif user_command == "10":
                print("""
                1 - Search persons by name
                2 - Search persons by phone number 
                """)
                user_command = input(">>>")

                if user_command == "1":
                    name = input("Name: ")
                    result = self.__services.search_persons_by_name(name)
                    if result == "":
                        print("No persons with this name found!")
                    else:
                        print(result)

                elif user_command == "2":
                    phone_number = input("Phone number: ")
                    result = self.__services.search_persons_by_phone_number(phone_number)
                    if result == "":
                        print("No persons with this phone number found!")
                    else:
                        print(result)

                else:
                    print("Invalid command. Please try again.")

            elif user_command == "11":
                date = input("Date with exactly this format ~DD.MM.YYYY~: ")
                try:
                    validate_date(date)
                except ValueError as ve:
                    print(f"\n{ve}\n")
                    continue
                result = self.__services.activities_for_a_date(date)
                if result == "":
                    print("No activities with this date found!")
                else:
                    print(result)

            elif user_command == "12":
                result = self.__services.busiest_days()
                if result == "":
                    print("There are no upcoming activities!")
                else:
                    print(result)

            elif user_command == "13":
                person_id = input("Person ID: ")
                result = self.__services.activities_with_a_person(person_id)
                if result == "":
                    print("No activities with this person found!")
                else:
                    print(result)

            elif user_command == "0":
                break

            else:
                print("Invalid command. Please try again.")
