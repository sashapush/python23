# Concerned with storing and retrieving books from csv file
# format: name,author,read\n

books_file = "books.txt"

#functions below are the content of the interface communicating with business logic

def create_book_table(): #so that there's a file we can read from, even if empty
    with open(books_file,'w') as file:
        pass


def add_book(name, author):
    with open(books_file,'a') as file: #a mode appends.
        file.write(f"{name},{author},0\n") #0 for False in read, 1 for True
def get_all_books():
    with open(books_file,'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()] #reads all the lines, incl \n and gives us each one/ [name,author,read],[name,author,read]

    return [ #[name,author,read],[name,author,read],[name,author,read]
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]

def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book["name"] == name:
            book["read"] = "1"
    _save_all_books(books) # "_" marks not callable function, "private" function, while P doesn't have concept of it


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(name):
    books = get_all_books()
    books = [books for book in books if book['name'] != name]
    _save_all_books(books)