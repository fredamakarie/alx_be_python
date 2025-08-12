class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = int(file_size)

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = int(page_count)

class Library:
    def __init__(self, books, title, author, file_size, page_count):
        self.books = books
        self.obj_book = Book(title, author)
        self.obj_ebook = EBook(file_size)
        self.obj_printbook = PrintBook(page_count)