#takes in entire html content and parses with beautiful soup
from bs4 import BeautifulSoup #external imports go above
from locators.books_page_locators import AllBooksPageLocators #internal below. Just a convention
from parsers.book_parser import BookParser
import logging
import re

logger = logging.getLogger('scraping.all_books_page') #child logger,config will be inherited



class AllBooksPage:
    def __init__(self, page_content):
        logger.debug('Parsing page content with Bs HTML parser.')
        self.soup = BeautifulSoup(page_content, 'html.parser')
    @property
    def books(self):
        logger.debug(f"Finding all book in the page using `{AllBooksPageLocators.BOOKS}`")
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)] #not selectone, select

    @property
    def page_count(self):
        logger.debug('Finding all number of pages available')
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        logger.info(f"Found `{content}` pages available")
        expression = 'Page [0-9]+ of ([0-9]+)'  # () is a group; + is 1 or more (I've used * and it's 0 or more
        matches = re.search(expression, content)
        pages = int(matches.group(1)) #print(matches.group(2)) #
        logger.debug(f"Extracted `{pages}` as integer")
        return pages
