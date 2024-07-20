#how to get data from quotes page
from bs4 import BeautifulSoup
from locators.quote_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser

class QuotesPage:
    def __init__(self,page): #entire html
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.soup.select(locator) #find each div we are looking for
        return [QuoteParser(e) for e in quote_tags] #and here we parse them in QuoteParser to find children inside
    #group of Object QuoteParser is returned
#main page = https://quotes.toscrape.com/