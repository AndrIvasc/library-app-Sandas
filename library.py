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

    def borrow_by_details(self, title: str, author: str) -> BookCopy:
        """
        Find an available copy by title and author, and then borrow it.
        :param title: str
        :param author: str
        :return: BookCopy
        """
        for copy in self._copies:
            if (copy.book.title.lower() == title.lower()
            and copy.book.author.lower() == author.lower()
            and copy.get_status() == "available"):
                copy.set_status("borrowed")
                return copy
            raise Exception(f"No available copy of '{title}' by '{author}'.")

    def return_copy(self, copy_id: str):
        """
        Marking the BookCopy with the given ID as available.
        Will raise error if copy with given ID is not found
        :param copy_id: str
        :return: None
        """
        for copy in self._copies:
            if copy.copy_id == copy_id:
                copy.return_copy()
                return
        raise ValueError(f"No copy of book was found with ID {copy_id}")

    def find_copies(self, query: str) -> List[BookCopy]:
        """
        Searching for copies of books whose title or author contains a query string. Its not case-sencitive.
        Returns a list sorted by publication year descending.
        :param query: str
        :return: List[BookCopy]
        """
        q = query.lower()
        matches = [c for c in self._copies
                   if q in c.book.title.lower() or q in c.book.author.lower()]

        return sorted(matches, key=lambda c: c.book.get_year(), reverse=True)

    def list_all_copies(self) -> List[BookCopy]:
        """
        Returns all copies in library unsorted
        """
        return list(self._copies)
