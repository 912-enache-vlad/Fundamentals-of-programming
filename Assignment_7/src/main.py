from ui.user_interface import user_interface
from services.services import Services, test_add_book_service
from RepositoriesFiles.bookRepositories import BookRepoMemory, BookRepoTextFile, BookRepoBinaryFile, BookRepoJsonFile
from src.unit_tests import Unit_tests

def main():
    # calling the unit test functions
    unit_tests = Unit_tests()
    unit_tests.test_all_add_books()
    test_add_book_service()

    repos = {
        "textfile": BookRepoTextFile,
        "memory": BookRepoMemory,
        "binaryfile": BookRepoBinaryFile,
        "jsonfile": BookRepoJsonFile
    }
    f = open("settings.properties", "r")
    repo_from_settings = f.readline()
    repo = repos[repo_from_settings.split("\n")[0]]()

    service = Services(repo)
    us = user_interface(service)
    us()


if __name__ == '__main__':
    main()


# books ideas:
# 1. "978-3-16-148410-10", "Dostoevsky", "The Brothers Karamazov"
# 2. "978-3-16-148410-26", "Jules Verne", "The Adventures of a Special Correspondent"
# 3. "978-3-16-148410-27", "Jules Verne", "The Adventures of a Young Englishman"
# 4. "978-3-16-148410-13", "Dostoevsky", "The Possessed"
# 5. "978-3-16-148410-14", "Dostoevsky", "The Devils"
# 6. "978-3-16-148410-15", "Dostoevsky", "The Gambler"
# 7. "978-3-16-148410-16", "Dostoevsky", "The House of the Dead"
# 8. "978-3-16-148410-17", "Dostoevsky", "Notes from Underground"
# 9. "978-3-16-148410-18", "Dostoevsky", "The Double"
# 10. "978-3-16-148410-19", "Dostoevsky", "The Adolescent"
# 11. "978-3-16-148410-20", "Jules Verne", "Around the World in Eighty Days"
# 12. "978-3-16-148410-21", "Jules Verne", "Twenty Thousand Leagues Under the Sea"
# 13. "978-3-16-148410-22", "Jules Verne", "The Mysterious Island"
# 14. "978-3-16-148410-23", "Jules Verne", "The Adventures of Captain Hatteras"
# 15. "978-3-16-148410-24", "Jules Verne", "The Adventures of Captain Grant"
# 16. "978-3-16-148410-25", "Jules Verne", "The Adventures of Three Englishmen and Three Russians"
