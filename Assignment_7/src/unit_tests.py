from src.services.services import Services
from src.RepositoriesFiles.bookRepositories import BookRepoMemory, BookRepoTextFile, BookRepoBinaryFile, BookRepoJsonFile
from src.domain.domain import Book
from typing import List

import os

class Unit_tests:
    def __init__(self):
        self.repo = None
        self.object1 = Book("978-3-16-148410-0", "Dostoevsky", "The Idiot")
        self.object2 = Book("978-3-16-148410-1", "Dostoevsky", "The Brothers Karamazov")
        self.object3 = Book("978-3-16-148410-2", "Dostoevsky", "Crime and Punishment")
        self.service = None

    def test_add_book_memory(self):
        self.repo = BookRepoMemory()
        self.service = Services(self.repo)
        self.service.add_book(self.object1)
        self.service.add_book(self.object2)
        self.service.add_book(self.object3)
        assert len(self.service.get_all_books()) == 3  # testing if it added 3 books
        assert self.compareBooks(self.service.get_all_books(), [self.object1, self.object2, self.object3]) == True
        try:    # testing if it raises an exception when adding a book that already exists
            self.service.add_book(self.object1)
            assert False
        except Exception:
            assert True
        assert len(self.service.get_all_books()) == 3
        assert self.compareBooks(self.service.get_all_books(), [self.object1, self.object2, self.object3]) == True

    def test_add_book_text_file(self):
        # deleting the file if it does exits
        if os.path.isfile("test_text_file.txt"):
            os.remove("test_text_file.txt")
        f = open("test_text_file.txt", "x")
        f.close()
        self.repo = BookRepoTextFile("test_text_file.txt")
        self.service = Services(self.repo)
        self.service.add_book(self.object1)
        self.service.add_book(self.object2)
        self.service.add_book(self.object3)
        assert len(self.service.get_all_books()) == 3
        assert self.compareBooks(self.service.get_all_books(), [self.object1, self.object2, self.object3]) == True
        try:
            self.service.add_book(self.object1)
            assert False
        except Exception:
            assert True
        assert len(self.service.get_all_books()) == 3
        assert self.compareBooks(self.service.get_all_books(), [self.object1, self.object2, self.object3]) == True
        if os.path.isfile("test_text_file.txt"):
            os.remove("test_text_file.txt")

    def test_add_book_binary_file(self):
        # deleting the file if it does exits
        if os.path.isfile("test_binary_file.pkl"):
            os.remove("test_binary_file.pkl")
        f = open("test_binary_file.pkl", "x")
        f.close()
        self.repo = BookRepoBinaryFile("test_binary_file.pkl")
        self.service = Services(self.repo)
        self.service.add_book(self.object1)
        self.service.add_book(self.object2)
        self.service.add_book(self.object3)
        assert len(self.service.get_all_books()) == 3
        assert self.compareBooks(self.service.get_all_books(), [self.object1, self.object2, self.object3]) == True
        try:
            self.service.add_book(self.object1)
            assert False
        except Exception:
            assert True
        assert len(self.service.get_all_books()) == 3
        assert self.compareBooks(self.service.get_all_books(), [self.object1, self.object2, self.object3]) == True
        if os.path.isfile("test_binary_file.pkl"):
            os.remove("test_binary_file.pkl")

    def test_add_book_json_file(self):
        if os.path.isfile("test_json_file.json"):
            os.remove("test_json_file.json")
        f = open("test_json_file.json", "x")
        f.close()
        self.repo = BookRepoJsonFile("test_json_file.json")
        self.service = Services(self.repo)
        self.service.add_book(self.object1)
        self.service.add_book(self.object2)
        self.service.add_book(self.object3)
        assert len(self.service.get_all_books()) == 3
        try:
            self.service.add_book(self.object1)
            assert False
        except Exception:
            assert True
        assert len(self.service.get_all_books()) == 3
        if os.path.isfile("test_json_file.json"):
            os.remove("test_json_file.json")

    @staticmethod
    def compareBooks(books1, books2:List[Book]):
        if len(books2) != len(books1):
            return False

        for i in range(len(books1)):
            if books1[i].isbn != books2[i].isbn:
                return False
            if books1[i].author != books2[i].author:
                return False
            if books1[i].title != books2[i].title:
                return False

        return True

    def test_all_add_books(self):
        self.test_add_book_memory()
        self.test_add_book_text_file()
        self.test_add_book_binary_file()
        self.test_add_book_json_file()


    def test_add_book_services(self):
        self.test_all_add_books()




