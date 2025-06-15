from typing import List
from models import Book, BookCopy


class Library:

    def __init__(self):
        self._copies: List[BookCopy] = []

    def add_new_copy(self, book: Book) -> BookCopy:
        """
        Creates a new BookCopy for the given book, store and and return it
        :param book: Book
        :return: BookCopy
        """
        copy = BookCopy(book)
        self._copies.append(copy)
        return copy

    # def borrow_copy(self, book: Book) -> BookCopy:
    #     """
    #     Finds the first available copy matching the given book and marks it as 'borrowed'
    #     Raise Value error if no available book exists
    #     :param book: Book
    #     :return: BookCopy
    #     """
    #     for copy in self._copies:
    #         if copy.book == book and copy.is_available():
    #             copy.borrow()
    #             return copy
    #     raise ValueError(f"No available copies for book {book} found")

    def borrow_copy(self, copy_id: str) -> BookCopy:
        """
        Mark the BookCopy with the given ID as borrowed.
        Raises ValueError if no such copy exists,
        or if it’s already borrowed.
        :param copy_id: str
        :return: BookCopy
        """
        for copy in self._copies:
            if copy.copy_id == copy_id:
                if copy.get_status() != "available":
                    raise ValueError(f"Copy {copy_id} is not available for borrowing.")
                copy.borrow()
                return copy
        raise ValueError(f"No copy of book was found with ID {copy_id}")

    def return_copy(self, copy_id: str) -> BookCopy:
        """
        Marking the BookCopy with the given ID as available.
        Will raise error if copy with given ID is not found
        :param copy_id: str
        :return: None
        """
        for copy in self._copies:
            if copy.copy_id == copy_id:
                copy.return_copy()
                return copy
        raise ValueError(f"No copy of book was found with ID {copy_id}")

    def find_copies(self, query: str) -> List[BookCopy]:
        """
        Search for copies whose title or author contains the query (case-insensitive),
        but if multiple copies share the same title and author, only returns the newest one.
        Results are sorted by publication year, descending.
        :param query: str
        :return: List[BookCopy]
        """
        q = query.lower()
        matches = [c for c in self._copies
                   if q in c.book.title.lower() or q in c.book.author.lower()]

        matches.sort(key=lambda c: c.book.get_year(), reverse=True)

        seen = set()
        unique = []
        for copy in matches:
            key = (copy.book.title.lower(), copy.book.author.lower())
            if key not in seen:
                seen.add(key)
                unique.append(copy)
        return unique

    def list_all_copies(self) -> List[BookCopy]:
        """
        Returns all copies in library unsorted
        """
        return list(self._copies)
