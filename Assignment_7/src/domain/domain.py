class Book:
    def __init__(self, isbn, author, title):
        self.__isbn = isbn
        self.__author = author
        self.__title = title

    # ---- only read for isbn ----
    @property
    def isbn(self):
        return self.__isbn

    # ---- read and write for author ----
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, new_author):
        self.__author = new_author

    # ---- read and write for title ----
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title


    def __str__(self):  #
        return f"{self.isbn}, {self.author}, {self.title}, - (isbn, author, title)"

    def to_dict(self):
        return {"isbn": self.isbn, "author": self.author, "title": self.title}

    def to_Book(self, dict):
        return Book(dict["isbn"], dict["author"], dict["title"])


if __name__ == "__main__":
    book1 = Book("978-3-16-148410-0", "Dan Brown", "DaVinvi Code")
    print(book1)
    book1.title = "Infernum"
    print(book1)
    book1.author = "Dostoievski"
    book1.title = "Crime and Punishment"
    print(book1)

