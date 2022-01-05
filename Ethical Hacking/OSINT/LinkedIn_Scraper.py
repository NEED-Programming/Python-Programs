#!bash/python

# py_Scrape will scrape and dump all information from LinkedIn into a txt. file.
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Find your Chromedriver location
driver = webdriver.Chrome("C:/Users/ispit/scraping/chromedriver.exe")

# Logging into LinkedIn
driver.get("https://linkedin.com/uas/login")
time.sleep(5)

username = driver.find_element_by_id("username")
username.send_keys("")  # Enter Your Email Address

pword = driver.find_element_by_id("password")
pword.send_keys("")  # Enter Your Password

driver.find_element_by_xpath("//button[@type='submit']").click()

# will have to look at script and input
# Headless will change that if you add
# web.browser(--headless, chromedriver
victim_name = print('What is the victims name?: ')
victim_name = str(input())

profile_url = 'https://www.linkedin.com/search/results/all/?keywords=' + victim_name
driver.get(profile_url)
time.sleep(5)

profile = driver.find_elements_by_xpath("//button[@type='main']").click()
driver.get(profile)