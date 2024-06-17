#update of wclasses file
import re
from bs4 import BeautifulSoup


ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>

</body></html>
'''
#1 create a class with methods inside
#2 create init method with soup object (so that instance of class will be created against some html code
#3 add (self) to every method so that the methods take in object of a class and function w/o change
#4 changed print statements in methods to return
#___
#This way we've done encapsulation - stored all the logic away inside the class

#Now we've renamed methods to simple name-rating etc
#By adding @property tag - we specify that a method return a property of a class object


class ParsedItem:
    """
    class to take in html page or partof it and find properties of an item in it
    """
    def __init__(self,page):
        self.soup = BeautifulSoup(page,'html.parser')

    @property
    def name(self):
    #item name
    #path of children up
        locator = ParsedItemLocators.NAME_LOCATOR #css locator
        item_link = self.soup.select_one(locator) #= <a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a>
        item_name = item_link.attrs['title'] #access the title property of string above
        return item_name

    @property
    def link(self):
        locator = ParsedItemLocators.LINK_LOCATOR # css locator
        item_link = self.soup.select_one(locator).attrs['href'] #relative link wo domain name
        return item_link

    # def find_item_price(self):
    #     #my way
    #     locator = ParsedItemLocators.PRICE_LOCATOR  # css locator
    #     expression = '£([0-9]+\.[0-9]+)' #() is a group; + is 1 or more (I've used * and it's 0 or more
    #     item_price = self.soup.select_one(locator).getText() #=£51.77 #lector did .string instead of .getText()
    #     matches = re.search(expression, item_price)
    #     print(matches.group(0)) #£51.77 (entire match)
    #     print(float(matches.group(1)))  #51.77 first thing in a brackets
    #     #lector way (if different)
    @property
    def rating(self):
        locator = ParsedItemLocators.RATING_LOCATOR  # css locator; star-rating Three - 2 css classes
        star_rating_tag = self.soup.select_one(locator)
        classes = star_rating_tag.attrs["class"] #we get list of values ['star-rating', 'Three']
        #we need to find out a class which is not 'star-rating'; list comprehension way
        rating_classes = [r for r in classes if r !='star-rating']
        # filter function way
        #rating_classes = filter(lambda x: x!='star-rating', classes) #TODO podumoi tut
        #item_rating
        print(classes)
        return rating_classes[0] #to return the element, not the full list

#next lesson - we add parsed item locators class, so that ParsedItem doesn't care about locator.
#Separating how and what.


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

item = ParsedItem(ITEM_HTML)
#print(item.find_item_rating())
print(item.link)
print(item.name)
print(item.rating)

#to summarize - 1 class to extract the data, 1 class to define where the data is on the page