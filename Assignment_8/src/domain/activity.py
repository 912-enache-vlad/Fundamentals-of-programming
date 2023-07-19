
class Activity:
    def __init__(self, activity_id, persons_id: list, date, time, description):
        self.__activity_id = activity_id
        self.__persons_id = persons_id
        self.__date = date
        self.__time = time
        self.__description = description

    @property
    def activity_id(self):
        return self.__activity_id

    @property
    def persons_id(self):
        return self.__persons_id

    @persons_id.setter
    def persons_id(self, new_persons_id):
        self.__persons_id = new_persons_id

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, new_date):
        self.__date = new_date

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, new_time):
        self.__time = new_time

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    def __str__(self):
        string = ""
        string += f"Activity ID: {self.__activity_id}\n"
        string += "Persons ID:\n"
        for person_id in self.__persons_id:
            string += f" - {person_id}\n"
        string += f"Date: {self.__date}\n"
        string += f"Time: {self.__time}\n"
        string += f"Description: {self.__description}\n\n"

        return string




