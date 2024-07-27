#how to get data from quotes page
import time
from typing import List
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.quote_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser
from selenium.common import NoSuchElementException
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

    def get_authors(self):
        #initial way of thinking - bad.
        #authors = [authors for authors in self.browser.find_elements(By.CSS_SELECTOR, QuotesPageLocators.AUTHORS_LIST)]
        #authors_name = [i.text for i in authors]
        #return authors_name
        #Lector did it simpler with list comprehension:
        return [option.text.strip() for option in self.author_dropdown.options]
    @property
    def tags_dropdown(self) -> Select:
        element = self.browser.find_element(By.CSS_SELECTOR, QuotesPageLocators.TAG_DROPDOWN)
        return Select(element)

    def get_tags(self):
        return [option.text.strip() for option in self.tags_dropdown.options] #we get the tags

    def select_tag(self, tag_name: str):
        self.tags_dropdown.select_by_visible_text(tag_name)

    @property
    def search_button(self):
        return self.browser.find_element(By.CSS_SELECTOR, QuotesPageLocators.SEARCH_BUTTON)

    def search_for_quotes(self, author_name:str, tag_name:str)-> List[QuoteParser]:
        self.select_author(author_name)
        #time.sleep(5) #5 seconds pause, but usually not appropriate to use it. Better to wait for something specific
        #impicit wait
        WebDriverWait(self.browser,10).until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR,QuotesPageLocators.TAG_DROPDOWN_VALUE_OPTION))
        try:
            self.select_tag(tag_name)
        except NoSuchElementException:
            raise InvalidTagForAuthorError(f"Author '{author_name} has not tag '{tag_name}'")
        self.search_button.click()
        return self.quotes

class InvalidTagForAuthorError(ValueError):
    pass