# importing information from the operating system
import os
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
            book = Book(data[0], data[1], data[2] == 'True', int(data[3]))
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
        output = [ book.title, book.author, str(book.read), str(book.id) ]
        output_str = separator.join(output)
        output_data.append(output_str)

    all_books_string = '\n'.join(output_data)

    return all_books_string
