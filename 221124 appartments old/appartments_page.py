#takes in entire html content and parses with beautiful soup
from bs4 import BeautifulSoup #external imports go above
from locators.books_page_locators import AllBooksPageLocators #internal below. Just a convention
from parsers.book_parser import BookParser
import logging
import re

logger = logging.getLogger('scraping.all_books_page') #child logger,config will be inherited



class AllBooksPage:
    def __init__(self, page_content):
        logger.debug('Parsing page content with Bs HTML parser.')
        self.soup = BeautifulSoup(page_content, 'html.parser')
    @property
    def books(self):
        logger.debug(f"Finding all book in the page using `{AllBooksPageLocators.BOOKS}`")
        return [for e in self.soup.select(AllBooksPageLocators.BOOKS)] #not selectone, select

    @property
    def page_count(self):
        logger.debug('Finding all number of pages available')
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        logger.info(f"Found `{content}` pages available")
        expression = 'Page [0-9]+ of ([0-9]+)'  # () is a group; + is 1 or more (I've used * and it's 0 or more
        matches = re.search(expression, content)
        pages = int(matches.group(1)) #print(matches.group(2)) #
        logger.debug(f"Extracted `{pages}` as integer")
        return pages
import re
import time

import requests
from bs4 import BeautifulSoup
import schedule


def scrape_text():
    # Send a GET request to the URL


    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the number of listings (Adjust the selector as necessary)
        regexp = re.compile("((1)-[0-9][0-9]) ogłoszeń z ([0-9][0-9])")
        text = soup.find(string=regexp)  # Replace with correct CSS class
        count = text.split("z ")
        return count[1].strip()
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None
# Wrap the job function to store its result
job_result = None

def job_wrapper():
    global job_result
    job_result = scrape_text()
    print("Job executed:", job_result)

# URL to monitor
# Monitor
initial_value = scrape_text()
print(f"Scraped data at time: " + time.ctime() + "\n" + f"Initial Value = {initial_value}")


print("Scheduler started. Polling every 5 minutes...")
schedule.every(5).minutes.do(job_wrapper)
# Keep the script running

def get_urls():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    url = "https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/cala-polska?distanceRadius=750&placeId=ChIJaQNS91stGUcRAtnDY1AAt24&limit=72&priceMin=2000&areaMin=42&priceMax=4500&by=LATEST&direction=DESC&viewType=listing&mapBounds=21.10565312320993%2C52.17806598316659%2C21.035314876790036%2C52.15197908416351"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the number of listings (Adjust the selector as necessary)
        url = soup.find_all()  # Replace with correct CSS class
        return count[1].strip()
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None

while True:
    schedule.run_pending()
    time.sleep(1)
    if job_result is not None:
        if job_result != initial_value:
            print(time.ctime(), "ALARMA")
