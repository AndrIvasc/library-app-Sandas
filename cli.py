from library import Library
from menu_option_logic import add_new_book, borrow_book, return_book, search_books, list_all_book


def print_menu():
    print("\n>>> Library menu <<<")
    print("1) Add new book copy")
    print("2) Borrow a book")
    print("3) Return a book")
    print("4) Search books")
    print("5) List all copies")
    print("0) Exit")


def main():
    library = Library()

    while True:
        print_menu()
        menu_choise = input("Choose and option: ").strip()

        if menu_choise == "1":
            print("\nAdd new book copy")
            add_new_book(library)
            input("\nPress Enter to continue...")

        elif menu_choise == "2":
            print("\nBorrow book")
            borrow_book(library)
            input("\nPress Enter to continue...")

        elif menu_choise == "3":
            print("\nReturn book")
            return_book(library)
            input("\nPress Enter to continue...")

        elif menu_choise == "4":
            print("\nSearch books")
            search_books(library)
            input("\nPress Enter to continue...")

        elif menu_choise == "5":
            print("\nShow all copies in the library")
            list_all_book(library)
            input("\nPress Enter to continue...")

        elif menu_choise == "0":
            print("Goodbye from your local library!")
            break

        else:
            print("You have entered a wrong choise. Please enter 1-5 or 0 to exit!")
            input("\nPress Enter to continue...")