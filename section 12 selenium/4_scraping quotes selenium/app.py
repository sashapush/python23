from selenium import webdriver
from pages.quotes_page import QuotesPage
chrome = webdriver.Chrome()
chrome.get("https://quotes.toscrape.com/")
#https://quotes.toscrape.com/search.aspx
page = QuotesPage(chrome) #and give the content to QuotesPage where constructor, which parses html to get self.soup

for quote in page.quotes:
    print(quote) #output is like <Quote “A day without sunshine is like, you know, night.”, by Steve Martin> by __repr__ method from Quote class
    #print(quote.content)