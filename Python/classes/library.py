# Define a Book class to represent a library book and manage its borrowing status
class Book:
    # Class attribute to count the total number of books
    total_books = 0
    
    # Constructor method to initialize each book's details
    def __init__(self, title, author, isbn, publication_year):
        # Instance attributes
        self.title = title  # Book's title
        self.author = author  # Book's author
        self.isbn = isbn  # Unique identifier for the book
        self.publication_year = publication_year  # Year the book was published
        self.__is_available = True  # Private attribute to track availability status
        self.borrower = None  # Tracks who borrowed the book
        
        # Increment the total book count each time a new book is created
        Book.total_books += 1

    # Method to borrow the book
    def borrow(self, borrower_name):
        if self.__is_available:
            self.__is_available = False  # Set availability to False
            self.borrower = borrower_name  # Set the borrower's name
            print(f"{borrower_name} has borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")

    # Method to return the book
    def return_book(self):
        if not self.__is_available:
            print(f"'{self.title}' returned by {self.borrower}.")
            self.__is_available = True  # Set availability to True
            self.borrower = None  # Clear the borrower's name
        else:
            print(f"'{self.title}' is not currently borrowed.")
    
    # Method to check if the book is available
    def is_available(self):
        return self.__is_available

    # Method to display book information
    def display_info(self):
        availability = "Available" if self.__is_available else f"Borrowed by {self.borrower}"
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\n"
            f"Publication Year: {self.publication_year}\nStatus: {availability}")
    
    # Class method to display the total number of books
    @classmethod
    def display_total_books(cls):
        print(f"Total books in library: {cls.total_books}")

# Example Usage
# Create instances of the Book class
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1925)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780060935467", 1960)

# Display information for each book
book1.display_info()
book2.display_info()

# Borrow and return actions
book1.borrow("Alice")         # Alice borrows The Great Gatsby
book1.display_info()           # Check status after borrowing
book1.borrow("Bob")            # Attempt to borrow again (should be unavailable)
book1.return_book()            # Alice returns the book
book1.display_info()           # Check status after returning

# Display total number of books using the class method
Book.display_total_books()

# Explanation of advanced class concepts:
# - **Private Attribute**: `__is_available` is a private attribute, only accessible within the class, to control the availability status.
# - **Encapsulation**: Methods `borrow`, `return_book`, and `is_available` provide controlled access to book status without exposing private details.
# - **Class Attribute and Class Method**: `total_books` is a class attribute shared by all Book instances, and `display_total_books` is a class method, allowing access to shared data.
# - **Instance Methods**: `display_info`, `borrow`, and `return_book` operate on individual book instances and manage specific data per book.
