# fileio.py
import os, datastore, ui

# making variables to store and call information from the operating system
DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')

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
                datastore.make_book_list(data)
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
    output_data = datastore.make_output_data()

    # Create data directory
    try:
        os.mkdir(DATA_DIR)
    except FileExistsError:
        pass # Ignore - if directory exists, don't need to do anything.


    with open(BOOKS_FILE_NAME, 'w') as f:
        f.write(output_data)

    with open(COUNTER_FILE_NAME, 'w') as f:
        f.write(str(counter))
