class Book:
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available: bool = True

    def borrow(self) -> None:
        """Marca el libro como prestado."""
        if self.is_available:
            self.is_available = False
        else:
            raise Exception(f"El libro '{self.title}' ya estÃ¡ prestado.")

    def return_book(self) -> None:
        """Marca el libro como disponible."""
        self.is_available = True

    def __str__(self) -> str:
        return f"{self.title} por {self.author} (ISBN: {self.isbn})"
