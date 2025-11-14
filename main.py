from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

# Pseudocode
# for book in library books:
#    if book avalible:
#      print book

def viewBooks():
    for book in library_books: # iterarte through ibrary_books
        if(book["available"] == True): # check if the book is available
            print(f"Book Id: {book["id"]}\nTitle: {book["title"]}\nBook Author: {book["author"]}\n") # print out book information

# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

# Pseudocode
# parameter userSearch
# listOfBooks = ""
# userSearch to lower case
# for book in library books:
#    if book genre to lower case = userSearch or book author to lower case = userSearch:
#      listOfBooks += book
# return listOfBooks

def search(userSearch):
    listOfBooks = [] # declare a variable for the list of books we will return
    for book in library_books: # iterate through library_books
        if(book["genre"].lower() == userSearch.lower() or book["author"].lower() == userSearch.lower()): # check if the books author or genre equals the users input
            listOfBooks += book # add the current book to list of books
    return listOfBooks # returns the list of books

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

# Pseudocode
# parmeters enteredId
# for book in libray books:
#    if book id = enterId:
#          if book avaliable:
#             book avaliable = false
#             book due date = 2 weeeks from now
#             book checkout counter += 1
#             return
#          else:
#             print error meassege
#             return
# print error message

def checkOutBook(bookId):
    for book in library_books: # iterate through libray books
        if(book["id"] == bookId): # check if the inserted id is equal to a books i
            if (book["available"] == True): # checks if the book is avaliable
                book["available"] = False # makes the book unavliable
                book["due_date"] = datetime.now() + timedelta(days=14) # sets the due date for the book 2 weeks from now
                book["checkouts"] += 1 # adds one to the books checkoouts
                return
            else:
                print("That book is already checked.") # prints a message about book being checked out
                return
        else:
            print("There is no book with that id.") # prints a error message
# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    checkOutBook("B1")
    checkOutBook("B2")
    checkOutBook("B1")
    pass
