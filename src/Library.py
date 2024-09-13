from src.Book import Book
from src.User import User


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []
        self.__checked_out_books = []
        self.__checked_in_books = []


    
    
    def get_books(self):
        return self.__books

    def get_users(self):
        return self.__users

    def get_checked_out_books(self):
        return self.__checked_out_books

    def get_checked_in_books(self):
        return self.__checked_in_books

    def add_book(self, isbn, title, author):
        book = Book(isbn, title, author)
        self.__books.append(book)

    def list_all_books(self):
        for book in self.__books:
            print(book)

    def check_out_book(self, isbn, dni, due_date):
        book = next((b for b in self.__books if b.get_isbn() == isbn), None)
        user = next((u for u in self.__users if u.get_dni() == dni), None)

        if not book or not user:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"
        if not book.is_available():
            return f"Book {isbn} is not available"

        book.set_available(False)
        book.increment_checkout_num()
        user.increment_checkouts()
        self.__checked_out_books.append([isbn, dni, due_date])

        return f"User {dni} checked out book {isbn}"

    def check_in_book(self, isbn, returned_date):
        book = next((b for b in self.__books if b.get_isbn() == isbn), None)

        if not book:
            return f"Book {isbn} is not available"

        if not any(b[0] == isbn for b in self.__checked_out_books):
            return f"Book {isbn} is not available"

        checkout_entry = next((b for b in self.__checked_out_books if b[0] == isbn), None)
        if checkout_entry:
            dni = checkout_entry[1]
            user = next((u for u in self.__users if u.get_dni() == dni), None)
            if user:
                user.increment_checkins()
            self.__checked_in_books.append([isbn, dni, returned_date])
            self.__checked_out_books.remove(checkout_entry)
            book.set_available(True)
        return f"Book {isbn} has been checked in"

    def add_user(self, dni, name):
        user = User(dni, name)
        self.__users.append(user)
