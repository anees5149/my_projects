import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pathlib import Path
import csv
import pyautogui
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


search = "spiderman"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
driver=webdriver.Chrome("C:\chromedriver.exe", chrome_options=chrome_options)
driver.implicitly_wait(5) # seconds
driver.get('https://www.reddit.com/')
driver.find_element_by_name('q').send_keys(search)
driver.find_element_by_name('q').send_keys(Keys.RETURN)
time.sleep(10)                
try:                                     
    driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div[1]/button/i').click()
except:
    driver.find_element_by_xpath("//*[@id='SHORTCUT_FOCUSABLE_DIV']/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div/div[1]/div[1]").click()
driver.find_element_by_xpath('/html/body/div[29]/div/a[3]/button/span').click()

time.sleep(10)
driver.close()
