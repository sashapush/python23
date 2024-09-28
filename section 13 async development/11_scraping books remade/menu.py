import logging
from app2_remade import books

logger = logging.getLogger('scraping.menu')

#runs app.py and gets the books
USER_CHOICE = '''Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalogue
- 'q' to exit

Enter your choice: '''


def print_best_books():
    logger.info("Finding best books by rating..")
    best_books = sorted(books, key= lambda x: x.rating, reverse=True)[:10]#sort the books by their rating, starting from the top; [:10] - slices to the top 10 elements
    #best_books = sorted(books, key= lambda x: x.rating*-1, reverse=True)[:10] teacher says to sort in descending way we can mutliply by -1
    for book in best_books:
        print(book)

'''List of 5 star books below'''
def print_five_star_books():
    logger.info("Finding best book by rating..")
    five_star_books = [book for book in books if book.rating == 5]
    for book in five_star_books:
        print(book)
def print_cheapest_books():
    logger.info("Finding cheapest books..")
    cheapest_books = sorted(books, key= lambda x: x.price)[:10]#sort the books by their rating, starting from the top; [:10] - slices to the top 10 elements
    #best_books = sorted(books, key= lambda x: x.rating*-1, reverse=True)[:10] teacher says to sort in descending way we can mutliply by -1
    for book in cheapest_books: #SHIFT-F6 to rename across all usages
        print(book)

# print("---BEST---")
# print_best_books()
# print("---CHEAPEST---")
# print_cheapest_books()


#to sort by 2 things:
def print_by2_books():
    best_books = sorted(books, key= lambda x: (x.rating*-1,x.price))[:10]#sort the books by their rating, starting from the top; [:10] - slices to the top 10 elements
    #best_books = sorted(books, key= lambda x: x.rating*-1, reverse=True)[:10] teacher says to sort in descending way we can mutliply by -1
    for book in best_books:
        print(book)
print("---2 criteria---")
print_by2_books()

books_generator = (x for x in books) #create a books generator. So that we can use next() of a said generator
def get_next_book():
    print(next(books_generator))

user_choices = {
    'b' : print_five_star_books, #the function, not the result. We don't call the functions since they would be run on dictionary filling
    'c': print_cheapest_books,
    'n': get_next_book
}
def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b','c','n'):
            user_choices[user_input]() # will give the function, associated with input inside dictionary, and run it via ()
        else:
            print("Please choose a valid command")
        user_input = input(USER_CHOICE)
    logger.debug("Terminating programm")


menu()