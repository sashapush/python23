import time
from datetime import datetime
import random

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
def main(random_list_value):
    to_click = random_list_value.find_element(By.CSS_SELECTOR, value=".single-pet-control-feed_button")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".single-pet-control-feed_button")))
    to_click.click()
    name = str(random_list_value.find_element(By.CSS_SELECTOR, value=".single-pet-name-inner").text)
    print("You've fed " + name)
    time.sleep(1)
    driver.save_screenshot(datetime.now().strftime("%Y%m%d-%H%M%S ") + name + ".png")

ass = []
counter = 0
while True:
    #Chrome
    #service_object = Service("c:\\Users\\Alex\\PycharmProjects\\chromedriver.exe")
    #driver = webdriver.Chrome(service=service_object)  # expected Service object from params.
    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("headless")
    #driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    #Firefox
    #service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\geckodriver.exe")
    #driver = webdriver.Firefox()#service=service_object)  # expected Service object from params.

    #Edge
    #service_object = Service("c:\\Users\\Alex\\PycharmProjects\\autopython_scrape\\msedgedriver.exe")
    #driver = webdriver.Edge(service=service_object)  # expected Service object from params.

    driver.maximize_window()
    driver.get("https://nakarmpsa.olx.pl/")
    #print(driver.title)
    #print(driver.current_url)
    time.sleep(4)
    ass = driver.find_elements(By.CSS_SELECTOR, value=".single-pet")
    temp = random.choice(ass)
    #to do catch exception
    #selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable

    try:
        main(temp)
        counter+=1
        if counter==-250:
            break
        print(f"Overall fed {counter} times")
    except:
        print("Message: element not interactable")
        driver.find_element(By.XPATH, value="//span[normalize-space()='2']").click()

    #driver.execute_script("arguments[0].scrollIntoView();", element)
    #ActionChains(driver).move_to_element(element).perform()
    #element.click()
    driver.close()
    #driver.find_elements(By.CSS_SELECTOR, value=".single-pet-control-feed")[0].click() click Iman
    # ass = driver.find_elements(By.CSS_SELECTOR, value=".single-pet")
    # choice = random_choice(ass)
    # driver.find_elements()
    # Close    the    new    window,    if that window no more required

