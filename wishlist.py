#Main program

# importing the ui.py program and the datastore program
import ui, datastore

# importing book from the book program
from book import Book

# main displayscreen for the program
def handle_choice(choice):

    # 1. Show unread books (wishlist)
    if choice == '1':
        show_unread()

    # 2. Show books that have been read
    elif choice == '2':
        show_read()

    # 3. Mark a book as read
    elif choice == '3':
        book_read()

    # 4. Add book to wishlist
    elif choice == '4':
        new_book()

    # 5. Delete a book from the wishlist
    elif choice == '5':
        delete_book()

    #6. Edit book Title or Author
    elif choice == '6':
        change_book_info()

    # q. Quit
    elif choice == 'q':
        quit()

    # message to show if input is not in the menu
    else:
        ui.message('Please enter a valid selection')

# function that goes to the datastore and the ui program for unread books
def show_unread():

    '''Fetch and show all unread books'''
    # getting all the unread books in the data store
    unread = datastore.get_books(read=False)
    # uses the ui program to print out the books or to say no books in list
    ui.show_list(unread)

# fuction that goes to datastore and ui for read books
def show_read():
    '''Fetch and show all read books'''
    # getting all the read books in the data store
    read = datastore.get_books(read=True)
    # uses the ui program to print out the books or to say no books in list
    ui.show_list(read)

# function that uses datastore and ui to change to read
def book_read():
    ''' Get choice from user, edit datastore, display success/error'''
    # uses ui to check and see if the book is in the system
    book_id = ui.ask_for_book_id()
    # if statment to give user feed back about results
    if datastore.set_read(book_id, True):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')

# function for adding a new book using ui and datastore
def new_book():
    '''Get info from user, add new book'''
    # calling the fuction getNewBookInfo from ui
    new_book = ui.get_new_book_info()
    # calling function from datastore to addBook to its list
    datastore.add_book(new_book)
    # output for user
    ui.message('Book added: ' + str(new_book))

# function for deleting a book using ui and datastore
def delete_book():
    # users ui to check and see if the book is in the system
    book_id = ui.ask_for_book_id()
    datastore.delete_book(book_id)




def change_book_info():
    ''' to change information about a book '''
    # uses ui to check and see if the book is in the system
    book_id = ui.ask_for_book_id()
    # if statment to give user feed back about results
    if datastore.edit_book(book_id):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')

# function for exiting the program and using datastore and ui
def quit():
    '''Perform shutdown tasks'''
    # calling function shutdown from datastore
    datastore.shutdown()
    # using function from ui to say bye
    ui.message('Bye!')

# main fuction for the program
def main():

    # calling setup function from datastore
    datastore.setup()

    # making quit and choice variables
    quit = 'q'
    choice = None

    # while loop to call display menu if the system isn't quiting
    while choice != quit:
        # getting displaymenu function from ui
        choice = ui.display_menu_get_choice()
        # calling the handleChoive function
        handle_choice(choice)

# calling main function if not from another program
if __name__ == '__main__':
    main()
