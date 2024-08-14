class Library:

  def __init__(self):
    self.books_in_library = []
    self.no_of_books = 0

  def add_book(self, book):

    self.books_in_library.append({
        "book_name": book.bookname,
        "bookid": book.bookid
    })
    self.no_of_books = len(self.books_in_library)

  def delete_book(self, id_or_name):

    for book in self.books_in_library:
      if book["bookid"] == id_or_name or book["book_name"] == id_or_name:
        print("removed=",book)
        self.books_in_library.remove(book)
        
        break
    self.no_of_books = len(self.books_in_library)

    self.no_of_books = len(self.books_in_library)

  def show(self):
    print(self.books_in_library)
    print(f"no of books {self.no_of_books}")


class Book:

  def __init__(self, name, id):
    self.bookname = name
    self.bookid = id

  @property
  def show(self):
    print(f"The book name is {self.bookname} and id is {self.bookid}")

  @show.setter
  def update(self, name, id):
    self.bookname = name
    self.bookid = id


library = Library()

b1 = Book("Harry Potter", 1)
library.add_book(b1)

b2 = Book("Python", 2)
library.add_book(b2)

b3 = Book("C++", 3)
library.add_book(b3)

#library.show()
library.delete_book(2)
library.show()
