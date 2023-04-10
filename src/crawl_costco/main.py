from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from crawler import crawl
from facebook_operator import openComment, openSeemore
from dotenv import load_dotenv

import time
import os

load_dotenv()
# the destination
url = "https://www.facebook.com/groups/1260448967306807"

options = Options()
options.add_argument("-en-US")
# Run in headless mode (without a visible browser window)
options.add_argument("--headless")
options.add_argument("--disable-notifications")
EMAIL = os.getenv("email")
PASSWORD = os.getenv("password")

driver = webdriver.Chrome(executable_path="../tools/chromedriver", options=options)
# driver.get("http://facebook.com")
# wait = WebDriverWait(driver, 30)
# email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
# email_field.send_keys(EMAIL)
# pass_field = wait.until(EC.visibility_of_element_located((By.NAME, 'pass')))
# pass_field.send_keys(PASSWORD)
# pass_field.send_keys(Keys.RETURN)
height = 0

try:
    driver.get(url)
except:
    print("url is wrong!")
time.sleep(3)

while True:
    driver.execute_script("window.scrollBy(0, 400)")
    time.sleep(2)
    openComment(driver)
    openSeemore(driver)
    cur_height = driver.execute_script(
        "return action=document.documentElement.scrollTop"
    )
    print("scroll")
    print(cur_height)
    print(height)
    if height == cur_height:
        break
    height = cur_height
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    crawl(soup)


driver.quit()
