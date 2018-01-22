# importing from book.py
from book import Book

# function to display menu chices
def display_menu_get_choice():

    '''Display choices for user, return users' selection'''

    print('''
        1. Show unread books (wishlist)
        2. Show books that have been read
        3. Mark a book as read
        4. Add book to wishlist
        5. Delete a book from the wishlist
        6. Edit book Title or Author
        7. Search for book in wishlist
        q. Quit
    ''')

    # getting input from user
    choice = input('Enter your selection: ')

    return choice

# function to show list for the user
def show_list(books):
    ''' Format and display a list of book objects'''

    # if no books in books prints no books
    if len(books) == 0:
        print ('* No book(s) *')
        return

    # for loop to print books in books
    for book in books:
        print(book)

    # printing the lenght of the list of books
    print('* {} book(s) *'.format(len(books)))

# function to get book id from user
def ask_for_book_id():

    ''' Ask user for book id, validate to ensure it is a positive integer '''

    # while loop so that it will keep asking till it gets a number
    while True:
        # try except to get a number
        try:
            # getting the book id from user
            id = int(input('Enter book id (title):'))
            # if to ensure number is greater than 0
            if id >= 0:
                return id
            # else statment to ask for a positive number
            else:
                print('Please enter a positive number ')
        except ValueError:
            print('Please enter an integer number')

# function to get book rating from user when they have finished the book
def get_book_rating():

    ''' Ask user for rating 1-5, validate to ensure it is a pos int 1-5 '''

    # while loop that will keep asking until it gets a valid input
    while True:
        # try execpt to get a number
        try:
            # get rating from user
            rating = int(input("Rate the book (1-5):"))
            # if to ensure number is between 1 and 5
            if rating > 0 and rating <= 5:
                return rating
            else:
                print("Please enter a number between 1 and 5 ")
        except ValueError:
            print("Please enter an integer number")


# function to get new book information
def get_new_book_info():

    ''' Get title and author of new book from user '''
    # getting input from the user
    title = input('Enter title: ')
    author = input('Enter author: ')
    return Book(title, author)

# function to prompt the user if they want to add a title that is already
# on the wishlist
def want_add_again():

    ''' Ask user if they want to add the book to the wishlist again '''
    # while loop that will keep asking until valid input
    while True:

        print("The book is already in the database.")
        answer = input("Would you like to add it again? (y/n)")

        if answer == "y":
            return "y"
        elif answer == "n":
            return "n"
        else:
            print("Please enter y for yes, or n for no")


# function to display a message to the user
def message(msg):
    '''Display a message to the user'''
    print(msg)
