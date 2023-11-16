class Book():
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages



book = Book("Roses", "Stephen King", 234)
print("Book name: ", book.name)
print("Book author: ", book.author)
print("Pages: ", book.pages)