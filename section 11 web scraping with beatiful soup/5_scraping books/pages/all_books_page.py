#takes in entire html content and parses with beautiful soup
from bs4 import BeautifulSoup #external imports go above
from locators.books_page_locators import AllBooksPageLocators #internal below. Just a convention
from parsers.book_parser import BookParser
class AllBooksPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')
    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)] #not selectone, select

