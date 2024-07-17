class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def check_out(self):
        self._is_checked_out = True
    def return_book(self):
        self._is_checked_out = False    
    def is_available(self):
        return not self._is_checked_out
    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self._books.append(book)
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False
    def list_available_books(self):
        print("Available books:")
        for book in self._books:
            if book.is_available():
                print(book)
                