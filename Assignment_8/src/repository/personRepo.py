from src.domain.person import Person


class PersonRepoException(Exception):
    pass


class PersonRepo:
    def __init__(self):
        self.__persons = []

    def remove_all_persons(self):
        self.__persons = []

    def add_person(self, person_id, name, phone_number):
        """
                Adds a person to the persons list
                :param person_id: the new person's id
                :param name: the new person's name
                :param phone_number: the new person's phone number
                :return: nothing
                """
        # validating the person id
        for person in self.__persons:
            if person.person_id == person_id:
                raise PersonRepoException("Person id already exists. Please try again with another id.\n")
        # validating the name
        if name == "":
            raise PersonRepoException("Empty name. Please try again.\n")
        # validating the phone number
        if phone_number == "":
            raise PersonRepoException("Empty phone number. Please try again.\n")


        self.__persons.append(Person(person_id, name, phone_number))

    def update_person(self, person_id, name, phone_number):
        """
                Updates a person from the persons list
                :param person_id: the person's id
                :param name: the person's new name
                :param phone_number: the person's new phone number
                :return: nothing
                """
        for person in self.__persons:
            if person.person_id == person_id:  # if I find the person with the given id
                person.name = name  # I update the name
                person.phone_number = phone_number  # and the phone number
                return
        raise PersonRepoException("Person not found!")

    def remove_person(self, person_id):
        """
                Removes a person from the persons list
                :param person_id: the person's id
                :return: nothing
        """
        for person in self.__persons:
            if person.person_id == person_id:
                self.__persons.remove(person)
                return
        raise PersonRepoException("Person not found!")

    def get_person(self, person_id):
        """
        Returns the person with the given id
        :param person_id: the person's id
        :return: Person object
        """
        for person in self.__persons:
            if person.person_id == person_id:
                return person
        return None



    def __str__(self):
        """
                Returns a string with all the persons
                :return: a string with all the persons
                """
        string = ""
        for person in self.__persons:
            string += str(person)

        return string

    def __len__(self):
        return len(self.__persons)

    def search_persons_by_name(self, name):
        result = ""
        for person in self.__persons:
            if name.lower() in person.name.lower():
                result += str(person) + "\n"
        return result

    def search_persons_by_phone_number(self, phone_number):
        result = ""
        for person in self.__persons:
            if phone_number in person.phone_number:
                result += str(person) + "\n"
        return result
