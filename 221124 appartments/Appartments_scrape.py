import re
import time
import requests
from bs4 import BeautifulSoup
import schedule
from playsound import playsound


base_url = "https://www.otodom.pl/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
url = base_url + "pl/wyniki/wynajem/mieszkanie/cala-polska?distanceRadius=750&placeId=ChIJaQNS91stGUcRAtnDY1AAt24&limit=72&priceMin=2000&areaMin=42&priceMax=4500&by=LATEST&direction=DESC&viewType=listing&mapBounds=21.10565312320993%2C52.17806598316659%2C21.035314876790036%2C52.15197908416351"
response = requests.get(url, headers=headers)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
# def scrape_text():
#         regexp = re.compile("((1)-[0-9][0-9]) ogłoszeń z ([0-9][0-9])")
#         text = soup.find(string=regexp)  # Replace with correct CSS class
#         count = text.split("z ")
#         return int(count[1].strip())
# Global variable to store combined task results
job_result = None
last_task_run_time = None

def get_urls():
    links = soup.find_all("a", class_="css-16vl3c1 e17g0c820")
    pruned_links = set()
    for link in links:
        if link["href"]:
            pruned_links.add(link["href"])
    return pruned_links

def job_wrapper():
    global job_result, last_task_run_time
    job_result = get_urls()
    last_task_run_time = time.time()
    print("Job executed")

#initial_counts = 50
#initial_links = {'/pl/oferta/mieszkanie-z-parking-ID4t8jp', '/pl/oferta/4-pietro-klimatyzacja-obok-royal-wilanow-ID4rR2z', '/pl/oferta/miasteczko-wilanow-2-pokoje-balkon-garaz-x2-ID4thnS', '/pl/oferta/miasteczko-wilanow-49m-2-pokoje-2x-garaz-ID4n2m0', '/pl/oferta/przestronne-2-pokoje-na-wilanowie-ID4tqBt', '/pl/oferta/dwupokojowe-mieszkanie-na-miasteczko-wilanow-ID4tvsh', '/pl/oferta/przestronne-wygodne-ciche-z-garazem-i-komorka-ID4sJKp', '/pl/oferta/3-pokoje-73m2-w-wilanowie-ID4rAtd', '/pl/oferta/mieszkanie-50-m2-z-garazem-w-miasteczku-wilanow-ID4tbOf', '/pl/oferta/wygodny-apartament-miasteczko-wilanow-ID4sL0d', '/pl/oferta/miasteczko-wilanow-2-pok-do-wynajecia-ID4sxr7', '/pl/oferta/mieszkanie-2-pokoje-ostoja-wilanow-garaz-komorka-ID4nzFp', '/pl/oferta/miasteczko-balkon-m-park-kom-lok-ID4t6RK', '/pl/oferta/kameralny-apartamentowiec-obornicka-29-ID4sVgc', '/pl/oferta/ciche-2-pokojowe-mieszkanie-54m2-garaz-balkon-ID4tpB7', '/pl/oferta/do-wynajecia-bezposrednio-2-pok-47m-z-ogrodkiem-ID4sMi4', '/pl/oferta/miasteczko-wilanow-przestronne-garaz-w-cenie-ID4t6lN', '/pl/oferta/klimczaka-10g-wilanow-sloneczne-2-pokoje-garaz-ID4strT', '/pl/oferta/widok-przestrzen-wilanow-46m2-2pokoje-4pietro-ID4tw1H', '/pl/oferta/klimatyczne-2-pok-mieszkanie-z-garazem-i-balkonem-ID4tmcV', '/pl/oferta/3-pokoje-mieszkanie-do-wynajecia-sarmacka-wilanow-ID4tb9C', '/pl/oferta/wilanow-2-pokoje-parking-podziemny-duzy-balkon-ID4tkhS', '/pl/oferta/wilanow-rzeczypospolitej-63m2-2-pokoje-garaz-ID4844n', '/pl/oferta/ladne-mieszkanie-2-pokojowe-w-wilanowie-ID4sOib', '/pl/oferta/wilanow-3-pokoje-50m2-po-gener-remoncie-wynajem-ID4tbgp', '/pl/oferta/2-pokojowe-mieszkanie-na-wilanowie-ID4sktS', '/pl/oferta/marconich-swietna-lokalizacja-przy-sarmackiej-4-ID4s7rc', '/pl/oferta/garaz-klimatyzacja-basen-w-budynku-ID4rkPG', '/pl/oferta/nowe-mieszkanie-w-wilanowie-ID4nT71', '/pl/oferta/eksluzywne-2-pokoje-2-miejsca-postojowe-ID4sCwb', '/pl/oferta/229979-ID4tnFs', '/pl/oferta/wyjatkowe-2-pokojowe-miasteczko-wilanow-ID4sMMP', '/pl/oferta/miasteczko-wilanow-58m2-3-pokoje-z-ogordkiem-ID4aFZQ', '/pl/oferta/wilanow-okazja-nowe-ID4sKNG', '/pl/oferta/apt-o-pow-52m2-2-pokoje-balkon-wilanow-lux-ID4tpkM', '/pl/oferta/2-pok-w-wysokim-standardzie-miasteczko-wilanow-ID4cy3K', '/pl/oferta/apartament-48-m2-z-tarasem-miasteczko-wilanow-ID4tmTb', '/pl/oferta/mieszkanie-2-pok-64m2-ostoja-wilanow-hlonda-2c-ID4sf0i', '/pl/oferta/mieszkanie-49m2-taras-40m2-garaz-w-cenie-klima-ID4rX7y', '/pl/oferta/2-pokoje-51m2-w-wilanowie-z-garazem-ID4mH1L', '/pl/oferta/mieszkanie-43-m-warszawa-ID4kE69', '/pl/oferta/mieszkanie-50-m-2-wilanow-ID3KQrq', '/pl/oferta/2-pokojowe-miasteczko-wilanow-bez-prowizji-ID4sWNV', '/pl/oferta/do-wynajecie-mieszkanie-2-pok-z-garazem-ID4rHlF', '/pl/oferta/atrakcyjny-apartament-na-wilanowie-80-m2-ID4sS3z', '/pl/oferta/luksusowe-2-pokojowe-ID4tr0E', '/pl/oferta/2-pokojowe-mieszkanie-na-wilanowie-ID4traK', '/pl/oferta/duze-mieszkanie-z-garazem-wilanow-ID4ty1A', '/pl/oferta/2-pokoje-miasteczko-wilanow-swietna-cena-ID4sMRc', '/pl/oferta/60-m-miasteczko-wilanow-garaz-w-cenie-ID4tx5K'}
initial_links = get_urls() #'/pl/oferta/ul-marconich-3-atrakcyjne-dwupokojowe-z-garazem-ID4tzrv',
#initial_counts = scrape_text()

print(f"Scraped data at time: " + time.ctime())
print("Scheduler started. Polling every 5 minutes...")
schedule.every(5).minutes.do(job_wrapper)
# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
    current_time = time.time()
    if last_task_run_time and current_time-last_task_run_time<2 and job_result:
        print(time.ctime(), "No changes", len(job_result))
        difference = job_result.difference(initial_links)
        if difference is not None:
            playsound('ta-ta.mp3')
            print('playing sound using  playsound')
            for element in difference:
                print(base_url+element)
                print(time.ctime(), "ALARMA")
                playsound('ta-ta.mp3')
                print('playing sound using  playsound')


