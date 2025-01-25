class Book:
    """A class representing a book with a title, author, and availability status."""
    
    def __init__(self, title, author):
        """Initialize a Book with title, author, and set it as available."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initially, the book is available

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned and available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"

class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize an empty list to store books."""
        self._books = []

