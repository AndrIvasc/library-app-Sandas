from models import Book, BookCopy
from library import Library


def enter_book_details():
    """
    Enter book details
    :return: str, str, int
    """
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    while True:
        year = input("Enter publication year: ").strip()
        if not year.isdigit():
            print("False input! Year must be a digit, try again")
            continue
        return title, author, int(year)


def add_new_book(library: Library):
    """
    Adding new book copy to list
    :param library: Library
    :return: None
    """
    title, author, year = enter_book_details()
    book = Book(title, author, year)
    copy = library.add_new_copy(book)
    print(f"Added new book copy {copy.copy_id} ({book.title}, {book.author}, {book.get_year()})")


def borrow_book(library: Library):
    """
    Borrowing book from the list of available books and setting status "borrowed"
    :param library: Library
    :return: None
    """
    print("\nAvailable copies to borrow:")
    status_list = print_status_book_list(library, "available")

    if not status_list:
        return
    else:
        copy_id = input("\nEnter the Copy ID to borrow: ").strip()
        try:
            copy = library.borrow_copy(copy_id)
            print(f"You borrowed copy {copy.copy_id} — "
                  f"{copy.book.title} by {copy.book.author} ({copy.book.get_year()})")
        except ValueError as e:
            print(e)


def return_book(library: Library):
    """
    Returning book from the list of borrowed books and setting status "available"
    :param library: Library
    :return: None
    """
    print("\nBorrowed copies to return:")
    status_list = print_status_book_list(library, "borrowed")

    if not status_list:
        return
    else:
        copy_id = input("\nEnter the Copy ID to return: ").strip()
        try:
            library.return_copy(copy_id)
            print(f"Returned copy {copy_id}")
        except ValueError as e:
            print(e)


def search_books(library: Library):
    """
    Searching book copy by author or title and returning list of books.
    Same book copy with different dates is shown only once with the newest date.
    :param library: Library
    :return: None
    """
    query = input("Search term (Title or author): ").strip()
    results = library.find_copies(query)
    if not results:
        print("No matches found...")
    else:
        print(f"Found {len(results)} copies: ")
        for c in results:
            status = c.get_status()
            print(f" *** [{status:^9}] {c.copy_id} - {c.book.title} by {c.book.author} ({c.book.get_year()})")


def list_all_book(library: Library):
    """
    List all copies of books in the library.
    :param library: Library
    :return: None
    """
    copies = library.list_all_copies()
    if not copies:
        print("No book copies in library were found!")
    else:
        for c in copies:
            status = c.get_status()
            print(f" *** [{status:^9}] {c.copy_id} – {c.book.title} by {c.book.author} ({c.book.get_year()})")


def print_status_book_list(library: Library, status: str):
    """
    Depending on the given status "borrowed" or "available" get sorted list and print it.
    :param library: Library
    :param status: str
    :return: status_list
    """
    status_list = sorted(
        (c for c in library.list_all_copies() if c.get_status() == status),
        key=lambda c: c.book.get_year(),
        reverse=True
    )
    if not status_list:
        print(f"  (No books are currently {status}.)")
    for c in status_list:
        print(f" {c.copy_id} – {c.book.title} by {c.book.author} ({c.book.get_year()})")

    return status_list
