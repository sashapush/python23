#how to get data from quotes page
from typing import List

from locators.quote_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class QuotesPage:
    def __init__(self, browser): #entire html
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        return [
            QuoteParser(e)
            for e in self.browser.find_elements(
                By.CSS_SELECTOR, QuotesPageLocators.QUOTE
            )
        ] #and here we parse them in QuoteParser to find children inside
    #group of Object QuoteParser is returned
#main page = https://quotes.toscrape.com/
    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element(By.CSS_SELECTOR, QuotesPageLocators.AUTHOR_DROPDOWN)
        return Select(element)

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)