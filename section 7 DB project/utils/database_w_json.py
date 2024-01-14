# Concerned with storing and retrieving books from csv file
# format: name,author,read\n
import json

"""
File example (list of dictionaries, since json is dictionary lol
[
{
'name': 'Clean Code',
'author': 'Robert',
'read': True
}
]
"""
books_file = "books.json"
# functions below are the content of the interface communicating with business logic

def create_book_table():  # so that there's a file we can read from, even if empty
    with open(books_file, 'w') as file:
        json.dump([], file) #since json library can't work with empty files - we dump empty list


def add_book(name, author):
    books = get_all_books()
    books.append({'name': name, "author": author, "read": False})
    _save_all_books(books)  # save all books once we updated with .append


def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books,file)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book["name"] == name:
            book["read"] = True
    _save_all_books(books)  # "_" marks not callable function, "private" function, while P doesn't have concept of it


def delete_book(name):
    books = get_all_books()
    books = [books for book in books if book['name'] != name]
    _save_all_books(books)