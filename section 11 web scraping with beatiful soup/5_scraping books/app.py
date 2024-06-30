import requests
from pages.all_books_page import AllBooksPage

page_content = requests.get("https://books.toscrape.com/").content #we get the content
page = AllBooksPage(page_content)

books = page.books #property of AllBooksPage class
# for book in books:
#     print(book)

#sort the books by rating and price




#todo add menu