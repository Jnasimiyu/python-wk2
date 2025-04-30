# Base class
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
    
    def describe(self):
        return f"'{self.title}' by {self.author} is a {self.genre} book."

    def read(self):
        return f"You start reading '{self.title}'."

# Subclass with inheritance
class EBook(Book):
    def __init__(self, title, author, genre, file_size):
        super().__init__(title, author, genre)
        self.file_size = file_size  # in MB
    
    def read(self):
        return f"You open the eBook '{self.title}' on your tablet. File size: {self.file_size}MB."

    def download(self):
        return f"Downloading '{self.title}'..."

# Usage
physical_book = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
ebook = EBook("Digital Fortress", "Dan Brown", "Thriller", 2.5)

print(physical_book.describe())
print(physical_book.read())
print(ebook.describe())
print(ebook.read())
print(ebook.download())
