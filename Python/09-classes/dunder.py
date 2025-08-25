class Book:
    total_books = 0  # Class attribute to track the total number of books

    # Constructor (dunder method) to initialize book details
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.__is_available = True
        self.borrower = None
        Book.total_books += 1

    # Borrow the book
    def borrow(self, borrower_name):
        if self.__is_available:
            self.__is_available = False
            self.borrower = borrower_name
            print(f"{borrower_name} has borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")

    # Return the book
    def return_book(self):
        if not self.__is_available:
            print(f"'{self.title}' returned by {self.borrower}.")
            self.__is_available = True
            self.borrower = None
        else:
            print(f"'{self.title}' is not currently borrowed.")

    # Check availability
    def is_available(self):
        return self.__is_available

    # Display book info
    def display_info(self):
        availability = "Available" if self.__is_available else f"Borrowed by {self.borrower}"
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\n"
              f"Publication Year: {self.publication_year}\nStatus: {availability}")

    @classmethod
    def display_total_books(cls):
        print(f"Total books in library: {cls.total_books}")

    # Dunder methods to customize built-in behavior:
    
    # Called when you use print(book)
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.publication_year})"
    
    # Called when you use repr(book) or in interactive shell
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}', year={self.publication_year})"
    
    # Called when using len(book)
    def __len__(self):
        return len(self.title)
    
    # Called when comparing two books using ==
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False

# Example usage:
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1925)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780060935467", 1960)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1925)

print(book1)          # Uses __str__: 'The Great Gatsby' by F. Scott Fitzgerald (1925)
print(repr(book2))    # Uses __repr__: Book(title='To Kill a Mockingbird', author='Harper Lee', isbn='9780060935467', year=1960)
print(len(book1))     # Uses __len__: length of the title → 16
print(book1 == book3) # Uses __eq__: True (same ISBN)
print(book1 == book2) # False
