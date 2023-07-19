from datetime import time, timedelta, date

from src.domain.activity import Activity


class ActivityRepoException(Exception):
    pass


class ActivityRepo:
    def __init__(self):
        self.__activities = []

    def remove_all_activities(self):
        self.__activities = []

    def add_activity(self, activity_id, persons_id, date, new_time, description):
        '''
                Adds an activity to the activities list
                :param activity_id: the new activity's id
                :param persons_id: the new activity's persons id
                :param date: the new activity's date
                :param time: the new activity's time
                :param description: the new activity's description
                :return:
                '''
        # checking if the activity already exists
        for activity in self.__activities:
            if activity.activity_id == activity_id:
                raise ActivityRepoException("An activity with this id already exists!")

        # checking if the new activity overlaps with another one
        times = new_time.split("-")
        start_new_time_str = times[0].strip()
        start_new_time_hour, start_time_minute = int(start_new_time_str.split(":")[0]), int(start_new_time_str.split(":")[1])
        start_new_time = time(start_new_time_hour, start_time_minute)
        end_new_time_str = times[1].strip()
        end_new_time_hour, end_time_minute = int(end_new_time_str.split(":")[0]), int(end_new_time_str.split(":")[1])
        end_new_time = time(end_new_time_hour, end_time_minute)

        for activity in self.__activities:
            times = activity.time.split("-")
            start_time_str = times[0].strip()
            start_time_hour, start_time_minute = int(start_time_str.split(":")[0]), int(start_time_str.split(":")[1])
            start_time = time(start_time_hour, start_time_minute)
            end_time_str = times[1].strip()
            end_time_hour, end_time_minute = int(end_time_str.split(":")[0]), int(end_time_str.split(":")[1])
            end_time = time(end_time_hour, end_time_minute)

            if activity.date == date:
                if start_new_time <= start_time <= end_new_time or start_new_time <= end_time <= end_new_time:
                    raise ActivityRepoException("The new activity overlaps with another one!")


        self.__activities.append(Activity(activity_id, persons_id, date, new_time, description))

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
        for activity in self.__activities:
            if activity.activity_id == activity_id:
                activity.persons_id = persons_id
                activity.date = date
                activity.time = time
                activity.description = description
                return
        raise ActivityRepoException("Activity not found!")

    def get_activity_by_id(self, activity_id):
        for activity in self.__activities:
            if activity.activity_id == activity_id:
                return activity
        return None

    def get_all_activities(self):
        return self.__activities

    def remove_activity(self, activity_id):
        """
                Removes an activity from the activities list
                :param activity_id: the activity's id
                :return: nothing
                """
        for activity in self.__activities:
            if activity.activity_id == activity_id:
                self.__activities.remove(activity)
                return
        raise ActivityRepoException("Activity not found!")

    def remove_person_from_activities(self, person_id):
        for activity in self.__activities:
            if person_id in activity.persons_id:
                activity.persons_id.remove(person_id)

    def __str__(self):
        """
                Returns a string with all the activities
                :return: a string with all the activities
                """
        string = ""
        for activity in self.__activities:
            string += str(activity)
        return string

    def __len__(self):
        return len(self.__activities)

    def search_activities_by_date(self, date):
        result = ""
        for activity in self.__activities:
            if activity.date == date:
                result += str(activity) + "\n"
        return result

    def search_activities_by_time(self, time):
        result = ""
        for activity in self.__activities:
            if time in activity.time:
                result += str(activity) + "\n"
        return result

    def search_activities_by_description(self, description):
        result = ""
        for activity in self.__activities:
            if description.lower() in activity.description.lower():
                result += str(activity) + "\n"
        return result

    def upcoming_activities(self):
        today = str(date.today().day) + "." + str(date.today().month) + "." + str(date.today().year)
        activities = []
        for activity in self.__activities:
            if activity.date >= today:
                activities.append(activity)
        return activities

