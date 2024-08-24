import logging
import requests
from pages.all_books_page import AllBooksPage
#this way we scrape 1 page
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO, #we can decrease level to INFO after app is stable
                    filename='logs.txt')
logger = logging.getLogger('scraping') #main logger, called scraping

logger.info("Loading books list..")
page_content = requests.get("https://books.toscrape.com/").content #we get the content of only 1 page out of 50

page = AllBooksPage(page_content)

books = page.books #property of AllBooksPage class
# for book in books:
#     print(book)

#this way we scrape all the 50 pages
for page_num in range(1, page.page_count): #1-49 (we have 1st page above)
    url = f"https://books.toscrape.com/catalogue/page-{page_num+1}.html"
    page_content = requests.get(url).content
    page = AllBooksPage(page_content)
    books.extend(page.books) #extend() is used for many elements, append() for 1