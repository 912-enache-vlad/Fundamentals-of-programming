import unittest

from src.domain.person import Person


class Test_Person(unittest.TestCase):
    def test_person(self):
        person = Person("1", "John", "123456789")
        self.assertEqual(person.person_id, '1')
        self.assertEqual(person.name, "John")
        self.assertEqual(person.phone_number, "123456789")

    def test_person_str(self):
        person = Person('1', "John", "123456789")
        self.assertEqual(str(person).strip(), "1, John, 123456789")

    def test_person_display_person_id(self):
        person = Person('1', "John", "123456789")
        self.assertEqual(person.display_person_id(), "1")

    def test_all(self):
        self.test_person()
        self.test_person_str()
        self.test_person_display_person_id()