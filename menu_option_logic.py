from models import Book, BookCopy
from library import Library


def enter_book_details():
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    while True:
        year = input("Enter publication year: ").strip()
        if not year.isdigit():
            print("False input! Year must be a digit, try again")
            continue
        return title, author, int(year)


def add_new_book(library: Library):
    title, author, year = enter_book_details()
    book = Book(title, author, year)
    copy = library.add_new_copy(book)
    print(f"Added new book copy {copy.copy_id} ({book.title}, {book.author}, {book.get_year()})")


def borrow_book(library: Library):
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    try:
        copy = library.borrow_by_details(title, author)
        print(f"You borrowed copy {copy.copy_id} ({copy.book.title}, {copy.book.author}, {copy.book.get_year()})")
    except Exception as e:
        print(e)


def return_book(library: Library):
    copy_id = input("Copy ID to return: ")
    try:
        library.return_copy(copy_id)
        print(f"Returned copy with {copy_id}")
    except Exception as e:
        print(e)


def search_books(library: Library):
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
    copies = library.list_all_copies()
    if not copies:
        print("No book copies in library were found!")
    else:
        for c in copies:
            status = c.get_status()
            print(f" *** [{status:^9}] {c.copy_id} – {c.book.title} by {c.book.author} ({c.book.get_year()})")
