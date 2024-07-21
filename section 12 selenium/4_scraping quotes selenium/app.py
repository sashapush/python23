from selenium import webdriver
from pages.quotes_page import QuotesPage
chrome = webdriver.Chrome()
chrome.get("https://quotes.toscrape.com/search.aspx")
#https://quotes.toscrape.com/search.aspx
#chrome.get("https://quotes.toscrape.com/")
page = QuotesPage(chrome) #and give the content to QuotesPage where constructor, which parses html to get self.soup
authors = page.get_authors()
author = input(f"Enter the author you'd like quotes from the list: {authors}")
page.select_author(author)

tags = page.get_tags()
print("Select one of these tags: [{}]".format(" | ".join(tags)))
selected_tag = input("Enter your tag: ")
page.select_tag(selected_tag)

page.search_button.click()

print(page.quotes)