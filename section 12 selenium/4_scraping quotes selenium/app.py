from selenium import webdriver
from pages.quotes_page import QuotesPage

#authors = page.get_authors()
author = input(f"Enter the author you'd like quotes from the list: ")
tag = input("Enter your tag: ")

chrome = webdriver.Chrome()
chrome.get("https://quotes.toscrape.com/search.aspx")
#chrome.get("https://quotes.toscrape.com/")
page = QuotesPage(chrome) #and give the content to QuotesPage where constructor, which parses html to get self.soup

print(page.search_for_quotes(author, tag))
