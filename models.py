import uuid


class Book:
    """
    Represents a book's metadata.
    """

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self._year = None
        self.set_year(year)

    def set_year(self, year: int):
        if not isinstance(year, int) or year <= 0:
            raise ValueError(f"The year must be a positive integer. You got {year}")
        self._year = year

    def get_year(self) -> int:
        return self._year

    def __eq__(self, other) -> bool:
        """
        Checks if the Book instance metadata is equal or not
        :param other: Book instance
        :return: bool
        """
        return (
                isinstance(other, Book)
                and self.title == other.title
                and self.author == other.author
                and self._year == other._year()
        )

    def __hash__(self) -> int:
        return hash((self.title, self.author, self._year))

    def __str__(self) -> str:
        return f"The book title is '{self.title}' by {self.author} written in ({self._year})"


class BookCopy:
    """
    Represents a specific copy of a Book, with a unique ID and a status.
    Status can be 'available' or 'borrowed'.
    """

    def __init__(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        self.book = book
        self.copy_id = str(uuid.uuid4())
        self._status = 'available'

    def set_status(self, status: str):
        if status not in ('available', 'borrowed'):
            raise ValueError(f"Status must be one of two 'available' or 'borrowed', but you got {status}")
        self._status = status

    def get_status(self) -> str:
        return self._status

    def is_available(self) -> bool:
        return self._status == 'available'

    def borrow(self):
        """Marking copy of book as borrowed"""
        if not self.is_available():
            raise ValueError(f"Copy {self.copy_id} is already borrowed")
        self.set_status("borrowed")

    def return_copy(self):
        """Mark this book copy as available"""
        if self.is_available():
            raise ValueError("Copy {self.copy_id} is already returned and available")
        self.set_status("available")

    def __str__(self) -> str:
        return f"Copy {self.copy_id}: {self.book} [{self._status}]"
