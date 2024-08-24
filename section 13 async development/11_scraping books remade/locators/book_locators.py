#define where book is located in a page
class BookLocators:
    #div.page_inner section, as seen in
    NAME_LOCATOR = "article.product_pod h3 a" #VARIABLE IN ALL CAPS is constant
    LINK_LOCATOR = "article.product_pod h3 a" #we'll need to access href property
    PRICE_LOCATOR = "article.product_pod p.price_color"
    STOCK_LOCATOR = "article.product_pod p.instock.availability"
    RATING_LOCATOR = "article.product_pod p.star-rating"