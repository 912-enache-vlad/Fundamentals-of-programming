import unittest

from src.repository.personRepo import PersonRepo, PersonRepoException


class Test_PersonRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.__person_repo = PersonRepo()
        self.__person_repo.add_person("1", "Vlad", "0751234567")
        self.__person_repo.add_person("2", "Andrei", "0751234568")
        self.__person_repo.add_person("3", "Ion", "0751234569")
        self.__person_repo.add_person("4", "Remus", "0751234561")

    def tearDown(self) -> None:
        self.__person_repo.remove_all_persons()
        self.__person_repo = None

    def test_add_person(self):
        # check if the person is added correctly
        self.__person_repo.add_person("5", "Maria", "0751234570")
        self.assertEqual(self.__person_repo.get_person("5").name, "Maria")
        self.assertEqual(self.__person_repo.get_person("5").phone_number, "0751234570")
        # check if the person already exists return an exception
        try:
            self.__person_repo.add_person("1", "Maria", "0751234570")
            self.assertTrue(False)
        except PersonRepoException:
            self.assertTrue(True)
        # check if the empty name return an exception
        try:
            self.__person_repo.add_person("6", "", "075123457")
            self.assertTrue(False)
        except PersonRepoException:
            self.assertTrue(True)
        # check if the empty phone number return an exception
        try:
            self.__person_repo.add_person("6", "Maria", "")
            self.assertTrue(False)
        except PersonRepoException:
            self.assertTrue(True)

    def test_get_person(self):
        self.assertEqual(self.__person_repo.get_person("1").name, "Vlad")
        self.assertEqual(self.__person_repo.get_person("1").phone_number, "0751234567")
        self.assertEqual(self.__person_repo.get_person('2').name, "Andrei")
        self.assertEqual(self.__person_repo.get_person('2').phone_number, "0751234568")
        self.assertEqual(self.__person_repo.get_person('3').name, "Ion")
        self.assertEqual(self.__person_repo.get_person('3').phone_number, "0751234569")
        self.assertEqual(self.__person_repo.get_person('4').name, "Remus")
        self.assertEqual(self.__person_repo.get_person('4').phone_number, "0751234561")

    def test_update_person(self):
        self.__person_repo.update_person("1", "George", "0711111111")
        self.assertEqual(self.__person_repo.get_person('1').name, "George")
        self.assertEqual(self.__person_repo.get_person('1').phone_number, "0711111111")
        try:
            self.__person_repo.update_person("7", "Alex", "0711111111")
            self.assertTrue(False)
        except PersonRepoException:
            self.assertTrue(True)

    def test_remove_person(self):
        self.__person_repo.remove_person("1")
        self.assertEqual(self.__person_repo.get_person("1"), None)
        try:
            self.__person_repo.remove_person("7")
            self.assertTrue(False)
        except PersonRepoException:
            self.assertTrue(True)

    # def test_str_

    def test_len_personRepo(self):
        self.assertEqual(len(self.__person_repo), 4)

    def test_search_persons_by_name(self):
        self.assertEqual(self.__person_repo.search_persons_by_name("Andrei").strip(), "2, Andrei, 0751234568")
        self.assertEqual(self.__person_repo.search_persons_by_name("Ion").strip(), "3, Ion, 0751234569")
        self.assertEqual(self.__person_repo.search_persons_by_name("Maria").strip(), "5, Maria, 0751234570")

    def test_search_persons_by_phone_number(self):
        self.assertEqual(self.__person_repo.search_persons_by_phone_number("0751234568").strip(), "2, Andrei, 0751234568")
        self.assertEqual(self.__person_repo.search_persons_by_phone_number("0751234569").strip(), "3, Ion, 0751234569")
        self.assertEqual(self.__person_repo.search_persons_by_phone_number("0751234561").strip(), "4, Remus, 0751234561")
        self.assertEqual(self.__person_repo.search_persons_by_phone_number("0751234570").strip(), "5, Maria, 0751234570")

    def test_str_personRepo(self):
        self.assertEqual(self.__person_repo.__str__(), "2, Andrei, 0751234568\n3, Ion, 0751234569\n4, Remus, 0751234561\n5, Maria, 0751234570\n")


    def test_all(self):
        self.test_add_person()
        self.test_get_person()
        self.test_update_person()
        self.test_remove_person()
        self.test_len_personRepo()
        self.test_search_persons_by_phone_number()
        self.test_search_persons_by_name()
        self.test_str_personRepo()

