from src.domain.domain import Book
from src.RepositoriesFiles.bookRepositories import BookRepoMemory


class Services:

    def __init__(self, repo):
        self.repo = repo

    def add_book(self, new_book: Book):
        """
        The function adds a new book to the repository
        :param new_book: the book to be added
        :return: nothing
        """
        self.repo.add_book(new_book)

    def get_all_books(self):
        return self.repo.get_all_books()

    def remove_book_by_title(self, starting_word: str):
        self.repo.remove_book_by_title(starting_word)

    def undo(self):
        self.repo.undo()

    def __str__(self):
        return self.repo.__str__()

    def file_is_empty(self):
        return self.repo.file_is_empty()


def test_add_book_service():
    books = []
    repo = BookRepoMemory()
    service = Services(repo)
    book1 = Book("978-3-16-148410-0", "Dostoevsky", "The Idiot")
    book2 = Book("978-3-16-148410-1", "Dostoevsky", "The Brothers Karamazov")
    book3 = Book("978-3-16-148410-2", "Dostoevsky", "Crime and Punishment")
    service.add_book(book1)
    service.add_book(book2)
    service.add_book(book3)
    assert len(service.get_all_books()) == 3
    assert service.get_all_books() == [book1, book2, book3]



