# importing information from the operating system, datetime library, and ui.py
import os, datetime, ui
# importing information from Book.py
from book import Book

# making variables to store and call information from the operating system
DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')

separator = '^^^'  # a string probably not in any valid data relating to a book

# creating the bookList
book_list = []
# creating variable counter
counter = 0

# function for the setup of getting the books from a file
def setup():
    ''' Read book info from file, if file exists. '''

    # calling the global variable counter
    global counter

    # try except action to see if there is a file on the system
    try :
        with open(BOOKS_FILE_NAME) as f:
            # fix for trying to read empty file and throwing IndexError
            if os.stat(BOOKS_FILE_NAME).st_size==0:
                pass
            else:
                data = f.read()
                make_book_list(data)
    except FileNotFoundError:
        # First time program has run. Assume no books.
        pass

    # try except action to see how many books are saved
    try:
        with open(COUNTER_FILE_NAME) as f:
            try:
                counter = int(f.read())
            except:
                counter = 0
    except:
        counter = len(book_list)

# function for shutdown to save all data to the files in the os
def shutdown():
    '''Save all data to a file - one for books, one for the current counter value, for persistent storage'''

    # calling the function make_output_data from this python
    output_data = make_output_data()

    # Create data directory
    try:
        os.mkdir(DATA_DIR)
    except FileExistsError:
        pass # Ignore - if directory exists, don't need to do anything.


    with open(BOOKS_FILE_NAME, 'w') as f:
        f.write(output_data)

    with open(COUNTER_FILE_NAME, 'w') as f:
        f.write(str(counter))

# function that gets the books
def get_books(**kwargs):
    ''' Return books from data store. With no arguments, returns everything. '''
    # calling the global variable book_list
    global book_list

    if len(kwargs) == 0:
        return book_list

    if 'read' in kwargs:
        read_books = [ book for book in book_list if book.read == kwargs['read'] ]
        return read_books


# function for adding books to db
def add_book(book):
    ''' Add to db, set id value, return Book'''

    # calling the global variable book_list
    global book_list

    # using the id from book
    book.id = generate_id()
    # adding the book to the end of the book_list
    book_list.append(book)

# function for deleting books from db
def delete_book(book_id, read):

    # calling the global variable book_list
    global book_list

    # goes through books in book_list
    # removes book with corresponding book_id
    for book in book_list:
        if book.id == book_id:
            book_list.remove(book)
            return True

    return False

def edit_book(book_id):
    ''' edit to db, return Book'''
    # calling the global variable book_list
    global book_list


    for book in book_list:
        if book.id == book_id:

            # setting variable to change them
            title = book.title
            author = book.author

            # asking user if they would like to change title
            changeTitle = input("Change Title? Y or N ")

            # if statement to change the Title
            if changeTitle == 'y' or changeTitle == 'Y':
                title = input('What do you want the new title for ' + title + " to be? ")
                book.title = title
                print("The new title will be " + title)

            # asking the user if they want to change the Author
            changeAuthor = input("Change Author? Y or N ")

            # if statement to change the author
            if changeAuthor == 'y' or changeAuthor == "Y":
                author = input("Who is the author for " + title + " ? ")
                book.author = author
            return True

    return False # return False if book id is not found

# function for creating ids for the book
def generate_id():
    # calling the global variable counter
    global counter
    # adding 1 to counter
    counter += 1
    # returning the varible counter
    return counter

# function to change if it is read
def set_read(book_id, read):
    '''Update book with given book_id to read. Return True if book is found in DB and update is made, False otherwise.'''

    # calling the global variable book_list
    global book_list


    for book in book_list:

        if book.id == book_id:
            book.read = True
            # uses datetime library
            # save current moment which is an object with month, day, year, etc
            # use month day and year from now object and set date_read to string
            now = datetime.datetime.now()
            book.date_read = str(now.month) + "/" + str(now.day) + "/" + str(now.year)
            # call ui.get_book_rating which will prompt user for a number 1-5
            book.rating = ui.get_book_rating()
            return True

    return False # return False if book id is not found


# function to make a book list
def make_book_list(string_from_file):
    ''' turn the string from the file into a list of Book objects'''

    try:
        # calling the global book_list
        global book_list

        # spliting the string from file to make it readible for user
        books_str = string_from_file.split('\n')


        for book_str in books_str:
            data = book_str.split(separator)
            book = Book(data[0], data[1], data[2] == 'True', int(data[3]), data[4], int(data[5]))
            book_list.append(book)
    except IndexError:
        pass


# function for making output data
def make_output_data():
    ''' create a string containing all data on books, for writing to output file'''
    # calling global book_list
    global book_list

    # making a list
    output_data = []

    # a for loop to make the book infor
    for book in book_list:
        output = [ book.title, book.author, str(book.read), str(book.id), book.date_read, str(book.rating) ]
        output_str = separator.join(output)
        output_data.append(output_str)

    all_books_string = '\n'.join(output_data)

    return all_books_string
