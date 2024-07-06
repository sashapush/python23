#define where books are located in a page
class AllBooksPageLocators:
    #div.page_inner section
    BOOKS = "div.page_inner section li.col-xs-6" #can be shortened from col-xs-6 col-sm-4 col-md-3 col-lg-3 if there are no other extra items which are not filtered by col-xs-6 only
    PAGER = "div.page_inner ul.pager li.current" #number of pages
