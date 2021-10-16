from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pathlib import Path
import csv

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
keyword = "DRIVER"
driver=webdriver.Chrome("C:\chromedriver.exe", chrome_options=chrome_options)
driver.get("https://memegine.com/")
time.sleep(10)                 
driver.find_element_by_xpath('//input[@class = "font-sans font-base w-full py-3 pl-7 text-sm text-black rounded-lg  focus:outline-non bg-white outline-none"]').send_keys(keyword)
driver.find_element_by_xpath('//input[@class = "font-sans font-base w-full py-3 pl-7 text-sm text-black rounded-lg  focus:outline-non bg-white outline-none"]').send_keys(Keys.RETURN)
driver.find_element_by_xpath('//input[@class = "font-sans font-base w-full py-3 pl-7 text-sm text-black rounded-lg  focus:outline-non bg-white outline-none"]').send_keys(Keys.RETURN)
time.sleep(5)
posts = []
n = 1
links = driver.find_elements_by_tag_name('a')
for link in links:
    post = link.get_attribute('href')
    if '/p' in post:
        posts.append(post)
time.sleep(5)
print(posts)

for post in posts:
    driver.get(post)
    time.sleep(4)
    url = driver.current_url
    try:                                                               
        page_name = driver.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[2]/div[2]/h1/a[1]').text
    except:    
        page_name = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[1]/div[2]").text
    try:
        description = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[1]/div[4]").text
    except:
        description = driver.find_element_by_xpath("//*[@id='__next']/main/div[2]/div/section/div/div[1]/div/div/div").text
    try:
        posted_by = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[1]/div[1]/a[1]").text
    except:
        posted_by = None
        time.sleep(4)
    with open("E:\my_projects\memegine2_datasheet.csv",'a',encoding='utf8') as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerow([keyword, url, page_name, description, posted_by])
        continue

print("over")
driver.close()
