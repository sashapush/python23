import requests
from bs4 import BeautifulSoup

page = requests.get("https://books.toscrape.com")
print(page.content) #html code

soup = BeautifulSoup(page.content,"html.parser")
print(soup.find('h1').string)
print(soup.select_one('a').attrs['href'])