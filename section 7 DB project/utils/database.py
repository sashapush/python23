# Concerned with storing and retrieving books from list
books = [] #global variable


def add_book(name, author):
    books.append({"name": name, "author": author, "read": False})

def get_all_books():
    return books


def mark_book_as_read(name):
    for book in books:
        if book["name"] == name:
            book["read"] = True

def delete_book(name):
    #lector's way, with local variable
    global books # stating that variable in local scope = variable in global scope
    books = [book for book in books if book["name"]!=name]  # list comprehension;add each book to new list if name != to the deletable one



    #my way(bad practise to modify list while iterating over it):
    # for book in books:
    #     if book["name"] == name:
    #         books.remove(book)