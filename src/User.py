from typing import List

class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.borrowed_books: List[str] = []

    def borrow_book(self, book: str) -> None:
        """Add a book to the user's borrowed books list."""
        self.borrowed_books.append(book)

    def return_book(self, book: str) -> None:
        """Remove a book from the user's borrowed books list."""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def has_borrowed(self, book: str) -> bool:
        """Check if the user has borrowed a specific book."""
        return book in self.borrowed_books

    def __str__(self) -> str:
        return f"User(name={self.name}, email={self.email})"
