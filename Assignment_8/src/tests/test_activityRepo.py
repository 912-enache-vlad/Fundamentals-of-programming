import unittest

from src.repository.activityRepo import ActivityRepo, ActivityRepoException


class Test_ActivityRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.activityRepo = ActivityRepo()
        self.activityRepo.add_activity("1", ['1', '2', '3'], "12.12.2022", "12:00 - 13:00", "Running")
        self.activityRepo.add_activity("2", ['3', '4', '4'], "21.12.2022", "15:00 - 16:00", "Football")
        self.activityRepo.add_activity("3", ['4', '5', '6'], "22.12.2022", "16:00 - 17:00", "Swimming")
        self.activityRepo.add_activity("4", ['7', '8', '9'], "23.12.2022", "17:00 - 18:00", "Volleyball")

    def tearDown(self) -> None:
        self.activityRepo.remove_all_activities()
        self.activityRepo = None

    def test_add_activity(self):
        self.activityRepo.add_activity("5", ['10', '11', '12'], "13.12.2022", "18:00 - 19:00", "Basketball")
        self.assertEqual(self.activityRepo.get_activity_by_id("5").date, "13.12.2022")
        self.assertEqual(self.activityRepo.get_activity_by_id("5").time, "18:00 - 19:00")
        self.assertEqual(self.activityRepo.get_activity_by_id("5").description, "Basketball")
        self.assertEqual(self.activityRepo.get_activity_by_id("5").persons_id, ['10', '11', '12'])
        # checking if giving the same id raises an exception
        try:
            self.activityRepo.add_activity("1", ['10', '11', '12'], "13.12.2022", "18:00 - 19:00", "Basketball")
            self.assertTrue(False)
        except ActivityRepoException:
            self.assertTrue(True)
       # checking if giving an activity which overlaps with another raises an exception
        try:
            self.activityRepo.add_activity("6", ['10', '11', '12'], "12.12.2022", "12:00 - 13:00", "Basketball")
            self.assertTrue(False)
        except ActivityRepoException:
            self.assertTrue(True)


    def test_get_activity_by_id(self):
        self.assertEqual(self.activityRepo.get_activity_by_id("1").date, "12.12.2022")
        self.assertEqual(self.activityRepo.get_activity_by_id("1").time, "12:00 - 13:00")
        self.assertEqual(self.activityRepo.get_activity_by_id("1").description, "Running")
        self.assertEqual(self.activityRepo.get_activity_by_id("1").persons_id, ['1', '2', '3'])

    def test_update_activity(self):
        self.activityRepo.update_activity("1", ['10', '11', '12'], "11.12.2022", "18:00 - 19:00", "Basketball")
        self.assertEqual(self.activityRepo.get_activity_by_id("1").date, "11.12.2022")
        self.assertEqual(self.activityRepo.get_activity_by_id("1").time, "18:00 - 19:00")
        self.assertEqual(self.activityRepo.get_activity_by_id("1").description, "Basketball")
        self.assertEqual(self.activityRepo.get_activity_by_id("1").persons_id, ['10', '11', '12'])
        # checking if giving an activity that doesn't exist raises an exception
        try:
            self.activityRepo.update_activity("9", ['10', '11', '12'], "11.12.2022", "18:00 - 19:00", "Basketball")
            self.assertTrue(False)
        except ActivityRepoException:
            self.assertTrue(True)

    def test_get_all_activities(self):
        self.assertEqual(self.activityRepo.get_all_activities(), [self.activityRepo.get_activity_by_id("1"), self.activityRepo.get_activity_by_id("2"), self.activityRepo.get_activity_by_id("3"), self.activityRepo.get_activity_by_id("4")])

    def test_str_activityRepo(self):
        result = self.activityRepo.__str__()
        self.assertEqual(self.activityRepo.__str__().strip(), "Activity ID: 1\nPersons ID:\n - 1\n - 2\n - 3\nDate: 12.12.2022\nTime: 12:00 - 13:00\nDescription: Running\n\nActivity ID: 2\nPersons ID:\n - 3\n - 4\n - 4\nDate: 21.12.2022\nTime: 15:00 - 16:00\nDescription: Football\n\nActivity ID: 3\nPersons ID:\n - 4\n - 5\n - 6\nDate: 22.12.2022\nTime: 16:00 - 17:00\nDescription: Swimming\n\nActivity ID: 4\nPersons ID:\n - 7\n - 8\n - 9\nDate: 23.12.2022\nTime: 17:00 - 18:00\nDescription: Volleyball\n\n".strip())


    def test_remove_activity(self):
        self.activityRepo.remove_activity("1")
        self.assertEqual(self.activityRepo.get_activity_by_id("1"), None)
        # checking if giving an activity that doesn't exist raises an exception
        try:
            self.activityRepo.remove_activity("9")
            self.assertTrue(False)
        except ActivityRepoException:
            self.assertTrue(True)

    def test_remove_person_from_activities(self):
        self.activityRepo.remove_person_from_activities("9")
        self.assertEqual(self.activityRepo.get_activity_by_id("4").persons_id, ['7', '8'])

    def test_search_activities_by_date(self):
        self.assertEqual(self.activityRepo.search_activities_by_date("21.12.2022").strip(), str(self.activityRepo.get_activity_by_id("2")).strip())
        
    def test_search_activities_by_time(self):
        self.assertEqual(self.activityRepo.search_activities_by_time("15:00 - 16:00").strip(), str(self.activityRepo.get_activity_by_id("2")).strip())
        
    def test_search_activities_by_description(self):
        self.assertEqual(self.activityRepo.search_activities_by_description("Football").strip(), str(self.activityRepo.get_activity_by_id("2")).strip())
        
    def test_upcoming_activities(self):
        self.assertEqual(self.activityRepo.upcoming_activities(), [self.activityRepo.get_activity_by_id("2"), self.activityRepo.get_activity_by_id("3"), self.activityRepo.get_activity_by_id("4")])

    def test_all(self):
        self.test_str_activityRepo()
        self.test_get_all_activities()
        self.test_add_activity()
        self.test_get_activity_by_id()
        self.test_update_activity()
        self.test_upcoming_activities()
        self.test_remove_activity()
        self.test_remove_person_from_activities()
        self.test_search_activities_by_date()
        self.test_search_activities_by_time()
        self.test_search_activities_by_description()

        


