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

soup = BeautifulSoup(ITEM_HTML,'html.parser')
def find_item_name():
#item name
#path of children up
    locator = 'article.product_pod h3 a' #css locator
    item_link = soup.select_one(locator) #= <a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a>
    item_name = item_link.attrs['title'] #access the title property of string above
    print(item_name)



def find_item_link():
    locator = 'article.product_pod a'  # css locator
    item_link = soup.select_one(locator).attrs['href'] #relative link wo domain name
    print(item_link)

def find_item_price():
    #my way
    locator = 'article.product_pod p.price_color'  # css locator
    expression = '£([0-9]+\.[0-9]+)' #() is a group; + is 1 or more (I've used * and it's 0 or more
    item_price = soup.select_one(locator).getText() #=£51.77 #lector did .string instead of .getText()
    matches = re.search(expression, item_price)
    print(matches.group(0)) #£51.77 (entire match)
    print(float(matches.group(1)))  #51.77 first thing in a brackets
    #lector way (if different)

def find_item_rating():
    locator = 'article.product_pod p.star-rating'  # css locator; star-rating Three - 2 css classes
    star_rating_tag = soup.select_one(locator)
    classes = star_rating_tag.attrs["class"] #we get list of values ['star-rating', 'Three']
    #we need to find out a class which is not 'star-rating'; list comprehension way
    rating_classes = [r for r in classes if r !='star-rating']
    # filter function way
    #rating_classes = filter(lambda x: x!='star-rating', classes) #TODO podumoi tut
    #item_rating
    print(classes)
    print(rating_classes[0]) #to return the element, not the full list

find_item_name()
find_item_link()
find_item_price()
find_item_rating()