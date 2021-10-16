import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pathlib import Path
import csv
import pyautogui


driver = webdriver.Chrome(r"C:\chromedriver.exe")
driver.implicitly_wait(5) # seconds
driver.get('https://www.instagram.com/')

driver.find_element_by_name("username").send_keys("username")
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_xpath("//button[@type= 'submit']").click()

driver.find_element_by_xpath("//button[text()= 'Not Now']").click()
driver.find_element_by_xpath("//button[text()= 'Not Now']").click()

driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[3]/a").click()
posts = []
time.sleep(5)
links = driver.find_elements_by_tag_name('a')
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
        posts.append(post)
print(posts)
for post in posts:
    driver.get(post)          
    time.sleep(5)
    pyautogui.click(731, 241)
    time.sleep(4)
    url = driver.current_url        
    try:
        user_name = driver.find_element_by_tag_name("h2").text   
    except NameError:
        user_name = driver.find_element_by_tag_name("h1").text
    except:
        user_name = None    

    try:
        followers = driver.find_element_by_tag_name("a").text
    except:
        followers = None
    try:                                                                     
        post = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[1]/span").text
    except NameError:
        post = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[1]/a").text
    except:
        post = None
    try:
        following = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").text
    except NameError:
        following = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/span").text
    except:
        following = None
    time.sleep(5)
    with open(r"E:\my_projects\insta2_datasheet.csv",'a',encoding='utf8') as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerow([url, user_name, followers, post, following])
        continue
