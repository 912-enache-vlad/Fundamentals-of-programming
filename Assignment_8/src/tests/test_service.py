import unittest

from src.repository.activityRepo import ActivityRepo
from src.repository.personRepo import PersonRepo, PersonRepoException
from src.services.services import Services


class Test_Service(unittest.TestCase):
    def setUp(self) -> None:
        self.__person_repo = PersonRepo()
        self.__activity_repo = ActivityRepo()
        self.__service = Services(self.__person_repo, self.__activity_repo)
        self.__service.add_person('1', "Vlad", "0741234567")
        self.__service.add_person('2', "George", "0741234568")

        self.__service.add_activity('1', ['1', '2'], "12.12.2022", "12:00 - 14:20", "description")

    def tearDown(self) -> None:
        self.__person_repo.remove_all_persons()
        self.__activity_repo.remove_all_activities()
        self.__person_repo = None
        self.__activity_repo = None
        self.__service = None

    def test_all(self):
        self.test_add_person()
        self.test_update_person()
        self.test_remove_person()
        self.test_add_activity()
        self.test_update_activity()
        self.test_remove_activity()
        self.test_list_activities()
        self.test_search_activities_by_date()
        self.test_search_activities_by_time()
        self.test_search_activities_by_description()
        self.test_search_persons_by_name()
        self.test_search_persons_by_phone_number()
        self.test_activities_for_a_date()
        self.test_busiest_days()
        self.test_activities_with_a_person()

    def test_add_person(self):
        self.__service.add_person('3', "Vasile", "0741234569")
        self.assertEqual(len(self.__person_repo), 3)
        self.assertEqual(self.__person_repo.get_person('3').name, "Vasile")
        self.assertEqual(self.__person_repo.get_person('3').phone_number, "0741234569")

    def test_update_person(self):
        self.__service.update_person('1', "Vlad Enache", "0711111111")
        self.assertEqual(self.__person_repo.get_person('1').name, "Vlad Enache")
        self.assertEqual(self.__person_repo.get_person('1').phone_number, "0711111111")

    def test_remove_person(self):
        self.__service.remove_person('1')
        self.assertEqual(len(self.__person_repo), 2)
        self.assertEqual(self.__activity_repo.get_activity_by_id('1').persons_id, ['2'])

    def test_add_activity(self):
        self.__service.add_activity('2', ['2'], "14.12.2022", "15:00 - 16:00", "another description")
        self.assertEqual(self.__activity_repo.get_activity_by_id('2').persons_id, ['2'])
        self.assertEqual(self.__activity_repo.get_activity_by_id('2').date, "14.12.2022")
        self.assertEqual(self.__activity_repo.get_activity_by_id('2').time, "15:00 - 16:00")
        self.assertEqual(self.__activity_repo.get_activity_by_id('2').description, "another description")
        # checking if giving a person that doesn't exist raises an exception
        try:
            self.__service.add_activity('3', ['100'], "14.12.2022", "12:00 - 13:00", "description")
            self.assertTrue(False)
        except PersonRepoException:
            self.assertTrue(True)

    def test_update_activity(self):
        self.__service.update_activity('1', ['2'], "12.12.2022", "12:00 - 13:00", "description")
        self.assertEqual(self.__activity_repo.get_activity_by_id('1').persons_id, ['2'])
        self.assertEqual(self.__activity_repo.get_activity_by_id('1').date, "12.12.2022")
        self.assertEqual(self.__activity_repo.get_activity_by_id('1').time, "12:00 - 13:00")
        self.assertEqual(self.__activity_repo.get_activity_by_id('1').description, "description")
        # checking if giving a person that doesn't exist raises an exception
        try:
            self.__service.update_activity('1', ['100'], "12.12.2022", "12:00 - 13:00", "description")
            self.assertTrue(False)
        except PersonRepoException:
            self.assertTrue(True)

    def test_remove_activity(self):
        self.__service.remove_activity('1')
        self.assertEqual(len(self.__activity_repo), 1)

    def test_list_activities(self):
        self.assertEqual(self.__service.list_all_activities().strip(), "Activity ID: 2\nPersons ID:\n - 2\nDate: 14.12.2022\nTime: 15:00 - 16:00\nDescription: another description\n\n".strip())

    def test_search_activities_by_date(self):
        self.assertEqual(self.__service.search_activities_by_date('14.12.2022').strip(), "Activity ID: 2\nPersons ID:\n - 2\nDate: 14.12.2022\nTime: 15:00 - 16:00\nDescription: another description\n\n".strip())

    def test_search_activities_by_time(self):
        self.assertEqual(self.__service.search_activities_by_time('15:00 - 16:00').strip(), "Activity ID: 2\nPersons ID:\n - 2\nDate: 14.12.2022\nTime: 15:00 - 16:00\nDescription: another description\n\n".strip())

    def test_search_activities_by_description(self):
        self.assertEqual(self.__service.search_activities_by_description('another description').strip(), "Activity ID: 2\nPersons ID:\n - 2\nDate: 14.12.2022\nTime: 15:00 - 16:00\nDescription: another description\n\n".strip())

    def test_search_persons_by_name(self):
        self.assertEqual(self.__service.search_persons_by_name('George').strip(), "2, George, 0741234568".strip())

    def test_search_persons_by_phone_number(self):
        self.assertEqual(self.__service.search_persons_by_phone_number('0741234568').strip(), "2, George, 0741234568".strip())


    def test_activities_for_a_date(self):
        self.assertEqual(self.__service.activities_for_a_date('14.12.2022').strip(), "Activity ID: 2\nPersons ID:\n - 2\nDate: 14.12.2022\nTime: 15:00 - 16:00\nDescription: another description\n\n".strip())


    def test_busiest_days(self):
        self.__service.add_activity('3', ['2'], "25.12.2022", "12:00 - 13:00", "description")
        self.assertEqual(self.__service.busiest_days().strip(), "Busiest upcoming days:\n25.12.2022: 60 minutes".strip())


    def test_activities_with_a_person(self):
        self.assertEqual(self.__service.activities_with_a_person('2').strip(), "Activities with person 2:Activity ID: 3\nPersons ID:\n - 2\nDate: 25.12.2022\nTime: 12:00 - 13:00\nDescription: description\n\n".strip())


