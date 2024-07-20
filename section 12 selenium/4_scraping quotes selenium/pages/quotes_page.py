#how to get data from quotes page

from locators.quote_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser
from selenium.webdriver.common.by import By


class QuotesPage:
    def __init__(self, browser): #entire html
        self.browser = browser

    @property
    def quotes(self):
        return [
            QuoteParser(e)
            for e in self.browser.find_elements(
                By.CSS_SELECTOR, QuotesPageLocators.QUOTE
            )
        ] #and here we parse them in QuoteParser to find children inside
    #group of Object QuoteParser is returned
#main page = https://quotes.toscrape.com/