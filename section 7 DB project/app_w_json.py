# text based application
from utils import database_w_json

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """
def menu():
    database_w_json.create_book_table()
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
    database_w_json.add_book(name, author)

def list_books():
    for book in database_w_json.get_all_books():
        read = 'YES' if book['read']  else 'NO' #if book['read'] = True
        print(f"{book['name']} by {book['author']} — Read: {read}")


def prompt_read_book():
    #read user input and mark book as read.
    name = input("Enter book name you've read:")
    database_w_json.mark_book_as_read(name)

def prompt_delete_book():
    name = input("Enter book name you want to delete:")
    database_w_json.delete_book(name)


menu()