from src.crawl_costco.facebook_operator import openComment, openSeemore
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options
driver = webdriver.Chrome(executable_path="../tools/chromedriver", options=options)
url = "https://www.facebook.com/groups/"
driver.get(url)
openSeemore(driver)
openComment(driver)