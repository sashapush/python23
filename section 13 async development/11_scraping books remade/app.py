import logging
import aiohttp
import asyncio
import time
import requests

from pages.all_books_page import AllBooksPage
#this way we scrape 1 page
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO, #we can decrease level to INFO after app is stable
                    filename='logs.txt')
logger = logging.getLogger('scraping') #main logger, called scraping

logger.info("Loading books list..")
page_content = requests.get("https://books.toscrape.com/").content #we get the content of only 1 page out of 50

page = AllBooksPage(page_content)

books = page.books #property of AllBooksPage class
# for book in books:
#     print(book)

urls = [f"https://books.toscrape.com/catalogue/page-{page_num+1}.html" for page_num in range(1, page.page_count)] #no longer iterating over it as below, but only creating urls
start = time.time()

#this way we scrape all the 50 pages
for page_num in range(1, page.page_count): #1-49 (we have 1st page above)
    url = f"https://books.toscrape.com/catalogue/page-{page_num+1}.html"
    page_content = requests.get(url).content
    page = AllBooksPage(page_content)
    books.extend(page.books) #extend() is used for many elements, append() for 1

async def fetch_page(url):
    page_start = time.time()
    async with asyncio.timeout(5): #timeout error is raised if (value) passes without function being done' can be tested with 0.2
        #create a client session from aiohttp
        async with aiohttp.ClientSession() as session: #create a session; can be suspended here
            async with session.get(url) as response: #get url; can be suspended here
                print(f"Page took {time.time() - page_start}")
                return response.status #return response status

#we also need a task scheduler

#to run 1 task
#loop.run_until_complete(fetch_page("https://google.com")) #we don't get response status - but a coroutine object.
async def main():
    tasks = [fetch_page("http://google.com") for i in range(50)]#to run multiple requests:
    await asyncio.gather(*tasks)  #*tasks is argument unpacking, = tasks[0],tasks[1] etc. gather() collects every task and runs it


start_time = time.time()
asyncio.run(main())
print(f'All took {time.time() - start_time}')