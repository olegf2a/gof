from .book import Book
from .book_collection import BookCollection


def demo() -> None:
    print("=== Iterator Pattern — Book Collection ===\n")

    collection = BookCollection()
    collection.add(Book("Orwell, George", "1984", 1949))
    collection.add(Book("Tolkien, J.R.R.", "The Hobbit", 1937))
    collection.add(Book("Huxley, Aldous", "Brave New World", 1932))
    collection.add(Book("Fitzgerald, F.S.", "The Great Gatsby", 1925))
    collection.add(Book("Camus, Albert", "The Stranger", 1942))

    header = f"{'Author':<20} | {'Title':<35} | {'Year'}"

    for order in ("author", "title", "year"):
        print(f"--- sorted by {order} ---")
        print(header)
        print("-" * len(header))
        for book in collection.create_iterator(order):
            print(book)
        print()


if __name__ == "__main__":
    demo()
