import json

from src.domain.domain import Book

import pickle


class Exception(Exception):
    pass


class BookRepoIterator:
    def __init__(self, book_repo):
        self._repo = book_repo
        self._index = -1

    def __next__(self):
        if self._index == len(self._repo):  # If I get to the end with the iteration
            raise StopIteration()

        self._index += 1
        return self._repo[self._index]


class BookRepoMemory:  # Memory Repository
    def __init__(self):
        self._books = []
        self._undo_list = []

    def file_is_empty(self):
        return True

    def add_book(self, new_book: Book):
        """
        The function adds a new book to the memory repository
        :param new_book: the book to be added
        :return: nothing
        """
        self._undo_list.append(self._books[:])
        # checking that the book doesn't already exist
        for book in self._books:
            if book.isbn == new_book.isbn:
                raise Exception("Book already exists!")
        self._books.append(new_book)

    def get_all_books(self):
        return self._books

    def __iter__(self):
        return BookRepoIterator(self)

    def remove_book_by_title(self, starting_word: str):
        self._undo_list.append(self._books[:])
        for book in self._books:
            if book.title.split(" ")[0] == starting_word:
                self._books.remove(book)

    def __len__(self):
        return len(self._books)

    def undo(self):
        if len(self._undo_list) == 0:
            raise Exception("Nothing to undo!")
        self._books = self._undo_list.pop()

    def __str__(self):  # displaying all books
        string = ""
        for book in self._books:
            string += f"{book} \n"
        return string


class BookRepoTextFile:
    def __init__(self, file_name = "RepositoriesFiles/book_text_file_repo.txt"):
        self.__file_name = file_name
        self.undo_list = []

    def file_is_empty(self):
        f = open(self.__file_name, "r")
        line = f.readline()
        if len(line) == 0:
            return True
        return False

    def add_book(self, new_book: Book):
        """
                The function adds a new book to the text file repository
                :param new_book: the book to be added
                :return: nothing
                """
        # checking if the new book doesn't already exist
        f = open(self.__file_name, "r")
        line = f.readline()
        while len(line) > 0:
            attributes = line.split(",")
            if attributes[0].strip() == new_book.isbn:
                raise Exception("Book already exists!")
            line = f.readline()
        f.close()

        # saving the state of the repository before the operation
        u = open(self.__file_name, "r")
        # print(u.read())
        self.undo_list.append(u.read())
        u.close()

        # appending the new book to the list of books
        f = open(self.__file_name, "a")
        f.write(f"{new_book} \n")  # writing the new book to the file
        f.close()

    def remove_book_by_title(self, starting_word: str):
        # saving the state of the repository before the operation
        u = open(self.__file_name, "r")
        self.undo_list.append(u.read())
        u.close()

        # removing the books that start with the given word
        books = []
        fin = open(self.__file_name, "r")
        line = fin.readline()  # reading one line at a time
        while len(line) > 0:
            if line == "\n":
                line = fin.readline()
                continue
            attributes = line.split(",")  # splitting the line into attributes
            isbn = attributes[0].strip()
            author = attributes[1].strip()
            title = attributes[2].strip()
            if title.split(" ")[0] != starting_word:  # if the title doesn't start with the word
                books.append(Book(isbn, author, title))  # adding the book to the list
            line = fin.readline()  # reading the next line
        fin.close()

        # writing the new list of books to the file
        fout = open(self.__file_name, "w")
        for book in books:
            fout.write(f"{book}\n")
        fout.close()

    def get_all_books(self):
        books = []
        f = open(self.__file_name, "r")
        line = f.readline()  # reading the first line
        while len(line) > 0:
            attributes = line.split(",")
            books.append(Book(attributes[0].strip(), attributes[1].strip(), attributes[2].strip()))  # using strip function to eliminate the spaces from the start and at the end
            line = f.readline()  # reading the next line
        f.close()
        return books

    def __iter__(self):
        return BookRepoIterator(self)

    def undo(self):
        if len(self.undo_list) == 0:
            raise Exception("No more undos!")
        f = open(self.__file_name, "w")
        f.write(self.undo_list.pop())
        f.close()

    def __str__(self):
        f = open(self.__file_name, "r")
        string = f.read()
        f.close()
        return string


class BookRepoBinaryFile:  # Binary File Repository
    def __init__(self, file_name = "RepositoriesFiles/book_binary_file_repo.bin"):
        self.__file_name = file_name
        self.undo_list = []

    def file_is_empty(self):
        f = open(self.__file_name, "rb")
        try:
            pickle.load(f)
        except EOFError:
            return True
        return False

    def add_book(self, new_book: Book):
        """
        The function adds a new book to the binary file repository
        :param new_book: the book to be added
        :return: nothing
        """
        # checking if the new book doesn't already exist
        f = open(self.__file_name, "rb")
        try:
            while True:
                book = pickle.load(f)
                if book.isbn == new_book.isbn:
                    raise Exception("Book already exists!")
        except EOFError:
            pass
        f.close()

        # saving the state of the repository before the operation
        u = open(self.__file_name, "rb")
        self.undo_list.append(u.read())
        u.close()

        # appending the new book to the list of books
        f = open(self.__file_name, "ab")
        pickle.dump(new_book, f)
        f.close()

    def remove_book_by_title(self, starting_word: str):
        # saving the state of the repository before the operation
        u = open(self.__file_name, "rb")
        self.undo_list.append(u.read())
        u.close()

        # removing the books that start with the given word
        books = []
        fin = open(self.__file_name, "rb")
        try:
            while True:
                book = pickle.load(fin)
                if book.title.split(" ")[0] != starting_word:
                    books.append(book)

        except EOFError:
            pass
        fin.close()

        # writing the new list of books to the file
        fout = open(self.__file_name, "wb")
        for book in books:
            pickle.dump(book, fout)
        fout.close()


    def get_all_books(self):
        books = []
        f = open(self.__file_name, "rb")    # opening the file in read binary mode
        try:
            while True:
                book = pickle.load(f)   # reading a book from the binary file
                books.append(book)      # saving the book to the books list
        except EOFError:
            pass
        f.close()       # closing the file
        return books

    def undo(self):
        if len(self.undo_list) == 0:
            raise Exception("No more undos!")
        f = open(self.__file_name, "wb")
        f.write(self.undo_list.pop()) # writing the last state of the repository
        f.close()

    def __str__(self):
        f = open(self.__file_name, "rb")
        string = ""
        try:
            while True:
                book = pickle.load(f)
                string += f"{book} \n"
        except EOFError:
            pass
        f.close()
        return string

    def __iter__(self):
        return BookRepoIterator(self)


class BookRepoJsonFile:
    def __init__(self, file_name = "RepositoriesFiles/book_json_file_repo.json"):
        self.__file_name = file_name
        self.undo_list = []

    def file_is_empty(self):
        f = open(self.__file_name, "r")
        string = f.read()
        f.close()
        if string == "":
            return True
        return False

    def add_book(self, new_book: Book):
        """
        The function adds a new book to the JSON file repository
        :param new_book: the book to be added
        :return: nothing
        """
        # checking if the new book doesn't already exist
        f = open(self.__file_name, "r")
        try:    # in case the file is empty
            books = json.load(f)
            f.close()
            for book in books:
                if book["isbn"] == new_book.isbn:
                    raise Exception("Book already exists!")
        except json.decoder.JSONDecodeError:
            f.close()
            books = []

        # saving the state of the repository before the operation
        try:
            u = open(self.__file_name, "r")
            self.undo_list.append(u.read())
            u.close()
        except:
            pass

        # appending the new book to the list of books
        f = open(self.__file_name, "w")
        books.append(new_book.to_dict())
        json.dump(books, f)
        f.close()

    def remove_book_by_title(self, starting_word: str):
        # saving the state of the repository before the operation
        u = open(self.__file_name, "r")
        self.undo_list.append(u.read())
        u.close()

        # removing the books that start with the given word
        books = []
        fin = open(self.__file_name, "r")
        books = json.load(fin)
        fin.close()
        books = [book for book in books if book["title"].split(" ")[0] != starting_word]

        # writing the new list of books to the file
        fout = open(self.__file_name, "w")
        json.dump(books, fout)
        fout.close()

    def get_all_books(self):
        books = []
        f = open(self.__file_name, "r")
        books = json.load(f)
        f.close()
        return books

    def undo(self):
        if len(self.undo_list) == 0:
            raise Exception("No more undos!")
        f = open(self.__file_name, "w")
        f.write(self.undo_list.pop())
        f.close()


    def __str__(self):
        f = open(self.__file_name, "r")
        books_dict = json.load(f)
        f.close()
        string = ""
        for book_dict in books_dict:
            book = Book(book_dict["isbn"], book_dict["title"], book_dict["author"])
            string += f"{book} \n"

        return string

    def __iter__(self):
        return BookRepoIterator(self)


if __name__ == "__main__":  # this is the main function where I am testing how things work
    book1 = Book("978-3-16-148410-5", "Fredrik Backman", "Britt-Marie Was Here")
    book2 = Book("978-3-16-148410-6", "Dostoevsky", "Crime and Punishment")
    book3 = Book("978-3-16-148410-7", "Dostoevsky", "The Idiot")
    book4 = Book("978-3-16-148410-8", "Dostoevsky", "The Brothers Karamazov")
    books = BookRepoBinaryFile()
    print(f"Before adding: \n{books}\n")
    books.add_book(book3)
    books.add_book(book2)
    books.add_book(book1)
    books.add_book(book4)
    print(f"After adding: \n{books}\n")
    books.remove_book_by_title("The")
    print(f"After removing: \n{books}\n")
    books.undo()
    print(f"After undo1: \n{books}\n")
    books.undo()
    print(f"After undo2: \n{books}\n")

