from datetime import timedelta

from src.domain.activity import Activity
from src.domain.person import Person
from src.repository.activityRepo import ActivityRepo
from src.repository.personRepo import PersonRepo, PersonRepoException


class Services:
    def __init__(self, person_repo: PersonRepo, activity_repo: ActivityRepo):
        self.__person_repo = person_repo
        self.__activity_repo = activity_repo

    def add_person(self, person_id, name, phone_number):
        """
        Adds a person to the persons list
        :param person_id: the new person's id
        :param name: the new person's name
        :param phone_number: the new person's phone number
        :return: nothing
        """
        self.__person_repo.add_person(person_id, name, phone_number)

    def update_person(self, person_id, name, phone_number):
        """
        Updates a person from the persons list
        :param person_id: the person's id
        :param name: the person's new name
        :param phone_number: the person's new phone number
        :return: nothing
        """
        self.__person_repo.update_person(person_id, name, phone_number)

    def remove_person(self, person_id):
        """
        Removes a person from the persons list
        :param person_id: the person's id
        :return: nothing
        """
        # removing the person from the persons list
        self.__person_repo.remove_person(person_id)
        # and from the activities
        self.__activity_repo.remove_person_from_activities(person_id)

    def list_all_persons(self):
        """
        Returns a string with all the persons
        :return: a string with all the persons
        """
        return str(self.__person_repo)

    def add_activity(self, activity_id, persons_id, date, time, description):
        '''
        Adds an activity to the activities list
        :param activity_id: the new activity's id
        :param persons_id: the new activity's persons id
        :param date: the new activity's date
        :param time: the new activity's time
        :param description: the new activity's description
        :return:
        '''
        # checking if the persons exist
        for person_id in persons_id:
            if self.__person_repo.get_person(person_id) is None:
                raise PersonRepoException(f"Person with id {person_id} does not exist!")
        self.__activity_repo.add_activity(activity_id, persons_id, date, time, description)

    def update_activity(self, activity_id, persons_id, date, time, description):
        """
        Updates an activity from the activities list
        :param activity_id: the activity's id
        :param persons_id: the activity's new persons id
        :param date: the activity's new date
        :param time: the activity's new time
        :param description: the activity's new description
        :return: nothing
        """
        for person_id in persons_id:
            if self.__person_repo.get_person(person_id) is None:
                raise PersonRepoException(f"Person with id {person_id} does not exist!")
        self.__activity_repo.update_activity(activity_id, persons_id, date, time, description)

    def remove_activity(self, activity_id):
        """
        Removes an activity from the activities list
        :param activity_id: the activity's id
        :return: nothing
        """
        self.__activity_repo.remove_activity(activity_id)

    def list_all_activities(self):
        """
        Returns a string with all the activities
        :return: a string with all the activities
        """
        return str(self.__activity_repo)

    def search_activities_by_date(self, date):
        return self.__activity_repo.search_activities_by_date(date)

    def search_activities_by_time(self, time):
        return self.__activity_repo.search_activities_by_time(time)

    def search_activities_by_description(self, description):
        return self.__activity_repo.search_activities_by_description(description)

    def search_persons_by_name(self, name):
        return self.__person_repo.search_persons_by_name(name)

    def search_persons_by_phone_number(self, phone_number):
        return self.__person_repo.search_persons_by_phone_number(phone_number)

    def activities_for_a_date(self, given_date):
        activities = []
        string = ""
        # saving the activities from a given date to a list
        for activity in self.__activity_repo.get_all_activities():
            if activity.date == given_date:
                activities.append(activity)
        # sorting the activities list by time
        activities.sort(key=lambda activity: activity.time)

        # creating the string to be returned
        for activity in activities:
            string += str(activity)

        return string

    def busiest_days(self):
        # creating a dictionary with the dates as keys and the used time as values
        date_used_time = {}
        for activity in self.__activity_repo.upcoming_activities():
            # computing the used time for each date
            times = activity.time.split("-")
            start_time_str = times[0].strip()
            start_time_hour, start_time_minute = int(start_time_str.split(":")[0]), int(start_time_str.split(":")[1])
            start_time = timedelta(hours=start_time_hour, minutes=start_time_minute)
            end_time_str = times[1].strip()
            end_time_hour, end_time_minute = int(end_time_str.split(":")[0]), int(end_time_str.split(":")[1])
            end_time = timedelta(hours=end_time_hour, minutes=end_time_minute)
            used_time = end_time - start_time
            used_time_min = int(used_time.total_seconds() // 60)

            if activity.date not in date_used_time:
                date_used_time[activity.date] = used_time_min
            else:
                date_used_time[activity.date] += used_time_min

        # sorting the dictionary by the used time
        sorted_date_used_time = sorted(date_used_time.items(), key=lambda item: item[1], reverse=True)

        string = "Busiest upcoming days:\n"
        # creating the string to be returned
        for date in sorted_date_used_time:
            string += f"{date[0]}: {date[1]} minutes\n"

        return string

    def activities_with_a_person(self, person_id):
        string = f"Activities with person {person_id}:"
        activities = []
        for activity in self.__activity_repo.upcoming_activities():
            if person_id in activity.persons_id:
                string += str(activity)

        return string


