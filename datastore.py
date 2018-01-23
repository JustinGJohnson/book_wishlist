# importing information from the operating system, datetime library, and ui.py
import os, datetime, ui
# importing information from Book.py
from book import Book

separator = '^^^'  # a string probably not in any valid data relating to a book

# creating the bookList
book_list = []
# creating variable counter
counter = 0

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

    # search part to find a book in the book list
    if 'search' in kwargs:
        question = input('What book are you looking for? ')
        searchBooks = [ book for book in book_list if book.title == question ]
        return searchBooks


# function for adding books to db
def add_book(book, read):
    ''' Add to db, set id value, return Book'''

    # calling the global variable book_list
    global book_list

    for b in book_list:
        if book.title == b.title:
            test = ui.want_add_again()
            if test == "y":
                book.id = generate_id()
                book_list.append(book)
                return True
            else:
                return False
    # using the id from book
    book.id = generate_id()
    # adding the book to the end of the book_list
    book_list.append(book)
    return True

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

            # setting variable name to change them
            title = book.title
            author = book.author
            
            # asking user if they would like to change title
            changeTitle = input("Change Title? Y or N ")

            # if statement to change the Title
            if changeTitle == 'y' or changeTitle == 'Y':
                title = input('What do you want the new title for ' + title + " to be? ")
                book.title = title
                print("The new title will be " + title)
            else:
                ui.message("No changes be made to the title.")
            # asking the user if they want to change the Author
            changeAuthor = input("Change Author? Y or N ")

            # if statement to change the author
            if changeAuthor == 'y' or changeAuthor == "Y":
                author = input("Who is the author for " + title + " ? ")
                book.author = author
            else:
                ui.message("No changes made to the author.")
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
