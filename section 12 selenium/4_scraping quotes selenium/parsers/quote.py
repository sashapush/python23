from locators.quote_locators import QuoteLocators
from selenium.webdriver.common.by import By


class QuoteParser:
    """
    Given one of the specific quote divs, find out the data about the quote(content,author,tags)
    """
    def __init__(self, parent):
        self.parent = parent #parent is the parent element, of a quote with content, author, tags inside, as children.


    def __repr__(self):
        return f"<Quote {self.content}, by {self.author}>"
    @property
    def content(self):
        locator = QuoteLocators.CONTENT #we use locator CONTENT
        return self.parent.find_element(By.CSS_SELECTOR, locator).text #and return content from said locator, not as .string for requests library

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR  # we use locator AUTHOR
        return self.parent.find_element(By.CSS_SELECTOR, locator).text  # and return content from said locator
    @property
    def tags(self):
        locator = QuoteLocators.TAGS #we use locator TAGS
        #return self.parent.select(locator)  # and return all tags the content from said locator
        #return [e.string for e in self.parent.select(locator)] #or we can extract text for each element
        return [e.string for e in self.find_elements(By.CSS_SELECTOR, locator)]