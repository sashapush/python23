#takes in entire html content and parses with beautiful soup
from bs4 import BeautifulSoup #external imports go above
from locators.books_page_locators import AllBooksPageLocators #internal below. Just a convention
from parsers.book_parser import BookParser
import re
class AllBooksPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')
    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)] #not selectone, select

    @property
    def page_count(self):
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        expression = 'Page [0-9]+ of ([0-9]+)'  # () is a group; + is 1 or more (I've used * and it's 0 or more
        matches = re.search(expression, content)
        pages = int(matches.group(1)) #print(matches.group(2)) #
        return pages
