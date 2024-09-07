import requests, aiohttp, time, asyncio, logging

from pages.all_books_page import AllBooksPage
 
 
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S', level=logging.DEBUG, filename='logs.txt')
logger = logging.getLogger('scraping')
logger.info('Loading books list...')
 
page_content = requests.get('http://books.toscrape.com').content
page = AllBooksPage(page_content)
 
books = page.books
 
async def fetch_page(url):
    page_start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start}...')
            return response.status
async def get_multiple_pages(*urls):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch_page(url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

async def main():
    urls = [f'http://books.toscrape.com/catalogue/page-{p+1}.html' for p in range(1, page.page_count)]
    pages = [get_multiple_pages(url) for url in urls]
    await asyncio.gather(*pages)  #*tasks is argument unpacking, = tasks[0],tasks[1] etc. gather() collects every task and runs it
    for page_content in pages:
         logger.debug('Creating AllBooksPage from page content.')
         books.extend(page.books)
    print(books)

start = time.time()
asyncio.run(main())
print(f'Total time is {time.time() - start}')

# for page_content in pages:
#     logger.debug('Creating AllBooksPage from page content.')
#     page = AllBooksPage(page_content)
#     books.extend(page.books)