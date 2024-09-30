# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.
# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.
# Existing Library Data:
# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# - Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.
welcome_message = "Welcome to the Library System!"
print(welcome_message)
to_do = input("What would you like to do? (1) Add a book (2) Remove a book (3) view all books: ")
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

while to_do:
    if to_do == "1":
        book_title = input("Enter the book title: ")
        book_author = input("Enter the book author: ")
        new_book = (book_title, book_author)
        if new_book in library:
            print("This book already exists in the library.")
        else:
            library.append(new_book)
            print("The book has been added to the library.")
    elif to_do == "2":
        book_title = input("Enter the book title: ")
        book_author = input("Enter the book author: ")
        new_book = (book_title, book_author)
        if new_book in library:
            library.remove(new_book)
            print("The book has been removed from the library.")
        else:
            print("This book does not exist in the library.")
    elif to_do == "3":
        print("The books in the library are:")
        for book in library:
            print(f"{book[0]} by {book[1]}")
    else:
        print("Invalid input. Please try again.")
    to_do = input("What would you like to do? (1) Add a book (2) Remove a book (3) view all books: ")
print("Thank you for using the Library System!")

def test_library_system():
    assert library == [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
    to_do = "1"
    book_title = "Animal Farm"
    book_author = "George Orwell"
    new_book = (book_title, book_author)
    library.append(new_book)
    assert library == [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley"), ("Animal Farm", "George Orwell")]
    to_do = "2"
    book_title = "Animal Farm"
    book_author = "George Orwell"
    new_book = (book_title, book_author)
    library.remove(new_book)
    assert library == [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
    to_do = "3"
    assert library == [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
    print("All tests pass.")
test_library_system()
