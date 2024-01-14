# to work as text based app, storing info in app memory and not persisting
from utils import database
# to work with files select - or see app_w_files2.py
#from utils import database_w_files

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """
def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()

        user_input = input(USER_CHOICE)

def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')
    database.add_book(name, author)

def list_books():
    for book in database.get_all_books():
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']} — Read: {read}")


def prompt_read_book():
    #read user input and mark book as read.
    name = input("Enter book name you've read:")
    database.mark_book_as_read(name)

def prompt_delete_book():
    name = input("Enter book name you want to delete:")
    database.delete_book(name)


menu()