import unittest
from models import Book, BookCopy


class TestBook(unittest.TestCase):
    def test_year_val(self):
        with self.assertRaises(ValueError):
            Book("Title", "Author", 0)
        with self.assertRaises(ValueError):
            Book("Title", "Author", -10)

        b = Book("Title", "Title", 2021)
        self.assertEqual(b.get_year(), 2021)

    def test_eq_and_hash(self):
        b1 = Book("Angel", "Dan", 2005)
        b2 = Book("Angel", "Dan", 2005)
        b3 = Book("Origin", "Dan", 1945)
        self.assertEqual(b1, b2)
        self.assertNotEqual(b1, b3)
        self.assertEqual(hash(b1), hash(b2))


class TestBookCopy(unittest.TestCase):
    def setUp(self):
        self.book = Book("Da Vin Chi", "Dan", 2000)

    def test_default_status_and_id(self):
        c = BookCopy(self.book)
        self.assertEqual(c.get_status(), "available")
        self.assertTrue(isinstance(c.copy_id, str) and len(c.copy_id) > 0)

    def test_borrow_and_return(self):
        c = BookCopy(self.book)
        c.borrow()
        self.assertEqual(c.get_status(), "borrowed")
        c.return_copy()
        self.assertEqual(c.get_status(), "available")

    def test_invalid_status(self):
        c = BookCopy(self.book)
        with self.assertRaises(ValueError):
            c.set_status("lost")


if __name__ == "__main__":
    unittest.main()
