from src.Book import Book
from src.User import User

class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []
        self.users: list[User] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book: Book) -> None:
        self.books.remove(book)

    def add_user(self, user: User) -> None:
        self.users.append(user)

    def remove_user(self, user: User) -> None:
        self.users.remove(user)

    def find_book(self, title: str) -> Book | None:
        for book in self.books:
            if book.title == title:
                return book
        return None

    def is_user_registered(self, user: User) -> bool:
        return user in self.users
