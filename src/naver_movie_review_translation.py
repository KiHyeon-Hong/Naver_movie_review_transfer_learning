from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

import re

browser = webdriver.Chrome("../chromdriver/chromedriver.exe")
browser.maximize_window()

browser.get("https://papago.naver.com/")

browser.find_element_by_xpath("/html/body/div/div/div[1]/section/div/div[1]/div[1]/div/div[3]/label").click()
browser.find_element_by_xpath("/html/body/div/div/div[1]/section/div/div[1]/div[1]/div/div[3]/label").send_keys('Test data')
browser.find_element_by_xpath("/html/body/div/div/div[1]/section/div/div[1]/div[1]/div/div[4]/div/button").click()
