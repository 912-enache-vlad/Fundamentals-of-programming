
class Person:
    def __init__(self, person_id, name, phone_number):
        self.__person_id = person_id
        self.__name = name
        self.__phone_number = phone_number

    @property
    def person_id(self):
        return self.__person_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, new_phone_number):
        self.__phone_number = new_phone_number

    def __str__(self):
        return f"{self.__person_id}, {self.__name}, {self.__phone_number}\n"

    def display_person_id(self):
        return f"{self.__person_id}"

