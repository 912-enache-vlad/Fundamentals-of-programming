import unittest

from src.domain.activity import Activity


class Test_Activity(unittest.TestCase):
    def test_person(self):
        activity = Activity("1",['1','2','3'], "01.01.2021", "10:00 - 12:00", "Zumba")
        self.assertEqual(activity.activity_id, '1')
        self.assertEqual(activity.persons_id, ['1','2','3'])
        self.assertEqual(activity.date, "01.01.2021")
        self.assertEqual(activity.time, "10:00 - 12:00")
        self.assertEqual(activity.description, "Zumba")

    def test_person_str(self):
        activity = Activity("1",['1','2','3'], "01.01.2021", "10:00 - 12:00", "Zumba")
        self.assertEqual(str(activity).strip(), "Activity ID: 1\nPersons ID:\n - 1\n - 2\n - 3\nDate: 01.01.2021\nTime: 10:00 - 12:00\nDescription: Zumba")

    def test_all(self):
        self.test_person()
        self.test_person_str()
