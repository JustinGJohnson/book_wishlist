# class for books
class Book:

    ''' Represents one book in a user's list of books'''
    # making the varible -1 if the is no id for the book
    NO_ID = -1

    # function init to set up the what variables are expected
    # id has the Default variable of no id
    def __init__(self, title, author, read=False, id=NO_ID):
        '''Default book is unread, and has no ID'''
        # making the variable for the class
        self.title = title
        self.author = author
        self.read = read
        self.id=id

    # to change the id for the book that is using the class
    def set_id(self, id):
        self.id = id

    # to add the read to the book if in user wants it
    def __str__(self):
        # default read variable is no
        read_str = 'no'
        # changes to yes if read is send
        if self.read:
            read_str = 'yes'

        # the id string and has a default readout of no id
        id_str = self.id
        if id == -1:
            id_str = '(no id)'

        # making the template for the book info for the user
        template = 'id: {} Title: {} Author: {} Read: {}'

        return template.format(id_str, self.title, self.author, read_str)

    # ???don't know what this is yet???    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.read == other.read and self.id==other.id
