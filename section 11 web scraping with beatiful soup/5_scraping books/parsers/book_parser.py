# reuse of the code, created in the section before
import re
import logging
from bs4 import BeautifulSoup
from locators.book_locators import BookLocators

logger = logging.getLogger('scarping.book_parser')
class BookParser:
    """
    class to take in html page or partof it and find properties of an item in it
    """
    #this is a class property.
    RATINGS = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5

    }  # it's not self.ratings, it can't be changed or accessed from object, only from class - BookParser.RATINGS

    def __init__(self, parent):  # parent is already a beautiful soup object
        logger.debug(f"New book parser created from `{parent}`") #big stuff, careful mate
        self.parent = parent

    def __repr__(self):
        return f"<Book {self.name}, costing {self.price}>, rating ({self.rating} stars)>"

    @property
    def name(self):
        # item name
        # path of children up
        logger.debug('Finding book name..')
        locator = BookLocators.NAME_LOCATOR  # css locator
        item_link = self.parent.select_one(
            locator)  # = <a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a>
        item_name = item_link.attrs['title']  # access the title property of string above
        logger.debug(f"Book name is `{item_name}` ")
        return item_name

    @property
    def link(self):
        logger.debug("Looking for the link")
        locator = BookLocators.LINK_LOCATOR  # css locator
        item_link = self.parent.select_one(locator).attrs['href']  # relative link wo domain name
        logger.debug(f"Link is found - `{item_link}`")
        return item_link

    @property
    def price(self):
        # my way
        logger.debug("Looking for price..")
        locator = BookLocators.PRICE_LOCATOR  # css locator
        expression = '£([0-9]+\.[0-9]+)'  # () is a group; + is 1 or more (I've used * and it's 0 or more
        item_price = self.parent.select_one(locator).string  # =£51.77 #lector did .string instead of .getText()
        matches = re.search(expression, item_price)
        float_price = float(matches.group(1)) # 51.77 first thing in a brackets
        logger.debug(f"Price is found: `{float_price}`")
        return float_price

    @property
    def rating(self):
        logger.debug("Looking for book rating..")
        locator = BookLocators.RATING_LOCATOR  # css locator; star-rating Three - 2 css classes
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs["class"]  # we get list of values ['star-rating', 'Three']
        # we need to find out a class which is not 'star-rating'; list comprehension way
        rating_classes = [r for r in classes if r != 'star-rating']
        #print(classes)
        rating_number = BookParser.RATINGS.get(rating_classes[0])#, default=9) #we get the text value from rating_classes[0] and class' property returns us the value of said key
        logger.debug(f"Book rating found {rating_number}..")
        #above None is not found; adding argument will be returned - 99 - if the value isn't found
        return rating_number  # to return the element, not the full list


class ParsedItemLocators:
    """
    Locators for an item in the HTML page.

    This allows us to easily see what our code will be looking at
    as well as change it quickly if we notice it is now different.
    """
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'


#item = ParsedItemLocators(ITEM_HTML)
# print(item.find_item_rating())
#print(item.link)
#print(item.name)
#print(item.rating)

# to summarize - 1 class to extract the data, 1 class to define where the data is on the page
