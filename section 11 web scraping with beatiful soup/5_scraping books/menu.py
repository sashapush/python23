from app import books
#runs app.py and gets the books
def print_best_books():
    best_books = sorted(books, key= lambda x: x.rating, reverse=True)[:10]#sort the books by their rating, starting from the top; [:10] - slices to the top 10 elements
    #best_books = sorted(books, key= lambda x: x.rating*-1, reverse=True)[:10] teacher says to sort in descending way we can mutliply by -1
    for book in best_books:
        print(book)

def print_cheapest_books():
    cheapest_books = sorted(books, key= lambda x: x.price)[:10]#sort the books by their rating, starting from the top; [:10] - slices to the top 10 elements
    #best_books = sorted(books, key= lambda x: x.rating*-1, reverse=True)[:10] teacher says to sort in descending way we can mutliply by -1
    for book in cheapest_books: #SHIFT-F6 to rename across all usages
        print(book)

print("---BEST---")
print_best_books()
print("---CHEAPEST---")
print_cheapest_books()


#to sort by 2 things:
def print_by2_books():
    best_books = sorted(books, key= lambda x: (x.rating*-1,x.price))[:10]#sort the books by their rating, starting from the top; [:10] - slices to the top 10 elements
    #best_books = sorted(books, key= lambda x: x.rating*-1, reverse=True)[:10] teacher says to sort in descending way we can mutliply by -1
    for book in best_books:
        print(book)
print("---2 criteria---")
print_by2_books()