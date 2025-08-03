class Book:
    def __init__(self, title, author, _is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []


        def add_book(self, Book):
            self._books.append(Book)

        def check_out_book(self, title):
            for Book in self._books:
                if Book.title == title and not Book._is_checked_out:
                    Book._is_checked_out = True
                    print(f"You checked out '{title}'.")
                    return
        print(f"Book '{Book.title}' is not available for checkout.")

        def return_book(self, title):
            for Book in self._books:
                if Book.title == title and Book.is_checked_out:
                    Book.is_checked_out = False
                    print(f"You returned '{title}'.")
                    return
        print(f"Book '{Book.title}' is not currently checked out.")

        def list_available_books(self):
            available_books = [Book for Book in self.books if not Book.is_checked_out]
            if not available_books:
                print("No books are currently available.")
            else:
                for Book in available_books:
                    print(Book)