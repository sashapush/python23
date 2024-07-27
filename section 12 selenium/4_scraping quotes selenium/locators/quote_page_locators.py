#define where quote is located in a page
class QuotesPageLocators:
    QUOTE = "div.quote" #VARIABLE IN ALL CAPS is constant
    AUTHOR_DROPDOWN = "select#author"
    AUTHORS_LIST = "select[id='author'] option"
    TAG_DROPDOWN = "select#tag"
    SEARCH_BUTTON = "input[value='Search']"
    TAG_DROPDOWN_VALUE_OPTION = "select#tag option[value]"
