# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 17:22:11 2022

@author: Sihan
"""
WEBADRESS='https://www.imdb.com/'
WEBDRIVERPATH='chromedriver.exe'


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


movies = []
poster_links = []

with open('OscarBP.txt', 'r') as f1:
    for line in f1.readlines():
        movies.append(line.split('-')[1].replace('"', ''))
        
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

browser = webdriver.Chrome(executable_path=WEBDRIVERPATH,   options=chrome_options)

wait = WebDriverWait(browser, 10)

browser.switch_to.window(browser.current_window_handle)
browser.implicitly_wait(30)

browser.get(WEBADRESS)

browser.switch_to.window(browser.current_window_handle)
browser.maximize_window()


for movie in movies:
    
    browser.find_element(By.ID, 'suggestion-search').click()
    browser.find_element(By.ID, 'suggestion-search').clear()
    browser.find_element(By.ID, 'suggestion-search').send_keys(movie)
    
    browser.find_element(By.CSS_SELECTOR, 'div.sc-17bafbdb-2 > ul.ipc-metadata-list > li.ipc-metadata-list-summary-item').click()
    
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img.ipc-image')))
    poster = browser.find_element(By.CSS_SELECTOR, 'img.ipc-image')
    poster_link = poster.get_attribute('srcset')
    
    poster_links.append(poster_link)
    
with open('OscarPosters.txt', 'w') as fo:
    for i in poster_links:
        fo.write(i + '\n')
    
    
    
    
    
    
    