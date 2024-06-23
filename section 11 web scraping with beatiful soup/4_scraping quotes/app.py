import requests
from pages.quotes_page import QuotesPage
page_content = requests.get("https://quotes.toscrape.com/").content #we get the content
page = QuotesPage(page_content) #and give the content to QuotesPage where constructor, which parses html to get self.soup

for quote in page.quotes:
    print(quote) #output is like <Quote “A day without sunshine is like, you know, night.”, by Steve Martin> by __repr__ method from Quote class
    #print(quote.content)