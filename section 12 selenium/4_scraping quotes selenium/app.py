from selenium import webdriver
from pages.quotes_page import QuotesPage
chrome = webdriver.Chrome()
chrome.get("https://quotes.toscrape.com/search.aspx")
#https://quotes.toscrape.com/search.aspx
#chrome.get("https://quotes.toscrape.com/")
page = QuotesPage(chrome) #and give the content to QuotesPage where constructor, which parses html to get self.soup

author = input("Enter the author you'd like quotes from: ")
page.select_author(author)
