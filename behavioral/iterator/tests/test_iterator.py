import unittest

from ..book import Book
from ..book_collection import BookCollection
from ..book_interface import BookInterface
from ..iterators import AuthorIterator, TitleIterator, YearIterator


def _make_collection() -> BookCollection:
    c = BookCollection()
    c.add(Book("Orwell, George", "1984", 1949))
    c.add(Book("Tolkien, J.R.R.", "The Hobbit", 1937))
    c.add(Book("Huxley, Aldous", "Brave New World", 1932))
    return c


class TestBook(unittest.TestCase):
    def test_implements_book_interface(self) -> None:
        book = Book("Orwell, George", "1984", 1949)
        self.assertIsInstance(book, BookInterface)

    def test_str_format(self) -> None:
        book = Book("Orwell, George", "1984", 1949)
        result = str(book)
        self.assertIn("Orwell, George", result)
        self.assertIn("1984", result)
        self.assertIn("1949", result)

    def test_fields(self) -> None:
        book = Book("Huxley, Aldous", "Brave New World", 1932)
        self.assertEqual(book.author, "Huxley, Aldous")
        self.assertEqual(book.title, "Brave New World")
        self.assertEqual(book.year, 1932)


class TestAuthorIterator(unittest.TestCase):
    def setUp(self) -> None:
        self.col = _make_collection()

    def test_sorted_ascending_by_author(self) -> None:
        books = list(self.col.create_iterator("author"))
        authors = [b.author for b in books]
        self.assertEqual(authors, sorted(authors))

    def test_first_author_alphabetically(self) -> None:
        it = self.col.create_iterator("author")
        self.assertEqual(next(it).author, "Huxley, Aldous")

    def test_has_next_true_when_items_remain(self) -> None:
        it = AuthorIterator([Book("A", "A", 2000)])
        self.assertTrue(it.has_next())

    def test_has_next_false_when_exhausted(self) -> None:
        it = AuthorIterator([Book("A", "A", 2000)])
        next(it)
        self.assertFalse(it.has_next())

    def test_stop_iteration_on_empty(self) -> None:
        it = AuthorIterator([])
        with self.assertRaises(StopIteration):
            next(it)

    def test_stop_iteration_when_exhausted(self) -> None:
        it = AuthorIterator([Book("A", "A", 2000)])
        next(it)
        with self.assertRaises(StopIteration):
            next(it)

    def test_returns_all_books(self) -> None:
        books = list(self.col.create_iterator("author"))
        self.assertEqual(len(books), 3)

    def test_iter_returns_self(self) -> None:
        it = self.col.create_iterator("author")
        self.assertIs(iter(it), it)


class TestTitleIterator(unittest.TestCase):
    def setUp(self) -> None:
        self.col = _make_collection()

    def test_sorted_ascending_by_title(self) -> None:
        books = list(self.col.create_iterator("title"))
        titles = [b.title for b in books]
        self.assertEqual(titles, sorted(titles))

    def test_first_title_alphabetically(self) -> None:
        it = self.col.create_iterator("title")
        self.assertEqual(next(it).title, "1984")

    def test_has_next_false_when_exhausted(self) -> None:
        it = TitleIterator([Book("A", "Z", 2000)])
        next(it)
        self.assertFalse(it.has_next())

    def test_stop_iteration_on_empty(self) -> None:
        it = TitleIterator([])
        with self.assertRaises(StopIteration):
            next(it)

    def test_returns_all_books(self) -> None:
        books = list(self.col.create_iterator("title"))
        self.assertEqual(len(books), 3)


class TestYearIterator(unittest.TestCase):
    def setUp(self) -> None:
        self.col = _make_collection()

    def test_sorted_ascending_by_year(self) -> None:
        books = list(self.col.create_iterator("year"))
        years = [b.year for b in books]
        self.assertEqual(years, sorted(years))

    def test_first_book_oldest(self) -> None:
        it = self.col.create_iterator("year")
        self.assertEqual(next(it).year, 1932)

    def test_last_book_newest(self) -> None:
        books = list(self.col.create_iterator("year"))
        self.assertEqual(books[-1].year, 1949)

    def test_has_next_false_when_exhausted(self) -> None:
        it = YearIterator([Book("A", "A", 2000)])
        next(it)
        self.assertFalse(it.has_next())

    def test_stop_iteration_on_empty(self) -> None:
        it = YearIterator([])
        with self.assertRaises(StopIteration):
            next(it)

    def test_returns_all_books(self) -> None:
        books = list(self.col.create_iterator("year"))
        self.assertEqual(len(books), 3)


class TestBookCollection(unittest.TestCase):
    def test_unknown_order_raises(self) -> None:
        col = _make_collection()
        with self.assertRaisesRegex(ValueError, "Unknown order"):
            col.create_iterator("price")

    def test_original_collection_not_mutated_by_year_iterator(self) -> None:
        col = _make_collection()
        original = [b.year for b in col._books]
        list(col.create_iterator("year"))
        self.assertEqual([b.year for b in col._books], original)

    def test_original_collection_not_mutated_by_author_iterator(self) -> None:
        col = _make_collection()
        original = [b.author for b in col._books]
        list(col.create_iterator("author"))
        self.assertEqual([b.author for b in col._books], original)

    def test_two_iterators_are_independent(self) -> None:
        col = _make_collection()
        it_year = col.create_iterator("year")
        it_author = col.create_iterator("author")
        next(it_year)
        self.assertEqual(next(it_author).author, "Huxley, Aldous")
        self.assertEqual(next(it_year).year, 1937)

    def test_add_increases_iteration_count(self) -> None:
        col = _make_collection()
        col.add(Book("Kafka, Franz", "The Trial", 1925))
        books = list(col.create_iterator("year"))
        self.assertEqual(len(books), 4)

    def test_empty_collection_iterator_exhausted_immediately(self) -> None:
        col = BookCollection()
        it = col.create_iterator("author")
        self.assertFalse(it.has_next())


if __name__ == "__main__":
    unittest.main()
