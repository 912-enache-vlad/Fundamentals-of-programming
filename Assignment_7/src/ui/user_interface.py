from src.services.services import Services
from src.domain.domain import Book

class user_interface:

    def __init__(self, service: Services):
        self.service = service

    def __call__(self):
        # having 10 programmatically generated entries in the application at start-up
        book1 = Book("978-3-16-148410-0", "Dostoevsky", "The Idiot")
        book2 = Book("978-3-16-148410-1", "Dan Brown", "Infernum")
        book3 = Book("978-3-16-148410-2", "Fredrik Backman", "Us Against You")
        book4 = Book("978-3-16-148410-3", "Dan Brown", "The Lost Symbol")
        book5 = Book("978-3-16-148410-4", "Dan Brown", "The Da Vinci Code")
        book6 = Book("978-3-16-148410-5", "Dale Carnegie", "How to Win Friends and Influence People")
        book7 = Book("978-3-16-148410-6", "Matthew Walker", "Why We Sleep")
        book8 = Book("978-3-16-148410-7", "Will Smith", "Will Smith: The Official Autobiography")
        book9 = Book("978-3-16-148410-8", "Fredrik Backman", "Britt-Marie Was Here")
        book10 = Book("978-3-16-148410-9", "Dostoevsky", "Crime and Punishment")
        book11 = Book("978-3-16-148410-10", "Dostoevsky", "The Brothers Karamazov")
        if self.service.file_is_empty() == True:
            try:
                self.service.add_book(book1)
            except Exception as re:
                print(f"book1 - {re}")
            try:
                self.service.add_book(book2)
            except Exception as re:
                print(f"book2 - {re}")
            try:
                self.service.add_book(book3)
            except Exception as re:
                print(f"book3 - {re}")
            try:
                self.service.add_book(book4)
            except Exception as re:
                print(f"book4 - {re}")
            try:
                self.service.add_book(book5)
            except Exception as re:
                print(f"book5 - {re}")
            try:
                self.service.add_book(book6)
            except Exception as re:
                print(f"book6 - {re}")
            try:
                self.service.add_book(book7)
            except Exception as re:
                print(f"book7 - {re}")
            try:
                self.service.add_book(book8)
            except Exception as re:
                print(f"book8 - {re}")
            try:
                self.service.add_book(book9)
            except Exception as re:
                print(f"book9 - {re}")
            try:
                self.service.add_book(book10)
            except Exception as re:
                print(f"book10 - {re}")
        else:
            pass
        while True:

            option = input("""
            1 - Add a book
            2 - Display the list of books
            3 - Filter the list so that book titles starting with a given word are deleted from the list.
            4 - Undo
            0 - Exit
            Choose a number:""")

            if option == '1':
                isbn = input("ISBN: ")
                author = input("Author: ")
                title = input("Title: ")
                try:
                    self.service.add_book(Book(isbn, author, title))
                except Exception as re:
                    print(re)

            elif option == '2':
                print(self.service)
            elif option == '3':
                starting_word = input("Starting word: ")
                self.service.remove_book_by_title(starting_word)
            elif option == '4':
                try:
                    self.service.undo()
                except Exception as re:
                    print(re)
            elif option == '0':
                return
            else:
                print("Invalid command. Please try again.")



