class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author  # Composition

    def display_info(self):
        print(f"'{self.title}' by {self.author.name} ({self.author.nationality})")

def run_question5():
    author1 = Author("J. K. Rowling", "British")
    book1 = Book("1997", author1)
    book1.display_info()
