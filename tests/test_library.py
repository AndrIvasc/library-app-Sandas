import unittest
from models import Book
from library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.lib = Library()

    def test_add_and_list(self):
        b = Book("Digital", "Dan", 2001)
        self.lib.add_new_copy(b)
        all_copies = self.lib.list_all_copies()
        self.assertEqual(len(all_copies), 1)
        self.assertEqual(all_copies[0].book, b)

    def test_borrow_and_return(self):
        b = Book("Digital", "Dan", 2001)
        c = self.lib.add_new_copy(b)

        # borrow works
        borrowed = self.lib.borrow_copy(c.copy_id)
        self.assertEqual(borrowed.get_status(), "borrowed")

        # borrowing again raises
        with self.assertRaises(ValueError):
            self.lib.borrow_copy(c.copy_id)

        # invalid ID raises
        with self.assertRaises(ValueError):
            self.lib.borrow_copy("random_borrowed_id")

        # return works
        self.lib.return_copy(c.copy_id)
        self.assertEqual(c.get_status(), "available")

        # returning again or bad ID raises
        with self.assertRaises(ValueError):
            self.lib.return_copy(c.copy_id)
        with self.assertRaises(ValueError):
            self.lib.return_copy("random_return_id")

    def test_find_copies_dedupe_and_sort(self):
        years = [1997, 1999, 1998]
        for yr in years:
            self.lib.add_new_copy(Book("Digital", "Dan", yr))

        results = self.lib.find_copies("digi")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].book.get_year(), 1999)

    def test_list_all_copies_returns_shallow_copy(self):
        b = Book("Harry", "J.k.", 2020)
        c = self.lib.add_new_copy(b)
        lst = self.lib.list_all_copies()
        lst.clear()
        self.assertEqual(len(self.lib.list_all_copies()), 1)


if __name__ == "__main__":
    unittest.main()
