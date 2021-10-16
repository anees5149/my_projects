from os import name
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv

keyword = "employees"
driver=webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://twitter.com/explore")
time.sleep(10)                 
driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input").send_keys(keyword)
driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input").send_keys(Keys.RETURN)
time.sleep(5)
posts= []
links = driver.find_elements_by_tag_name('a')
for link in links:
    post = link.get_attribute('href')
    if '/status/' in post:
        posts.append("/".join(post.split('/')[:6]))
posts = list(set(posts))      
for post in posts:
    driver.get(post)                        
    time.sleep(5)      
    url = driver.current_url 
    try:                                                  
        description = driver.find_element_by_xpath("//div[@class = 'css-1dbjc4n r-1s2bzr4']").text
    except:
        description = None
    time.sleep(5)    
    try:          
        name_ = driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > section > div > div > div:nth-child(1) > div > div > article > div > div > div > div.css-1dbjc4n.r-18u37iz.r-15zivkp > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci > div > div > div > div.css-1dbjc4n.r-1d09ksm.r-18u37iz.r-1wbh5a2').text.splitlines()
        username = name_[-1]
    except:
        username = None
    try:
        retweets = driver.find_element_by_xpath("//span[@class = 'css-901oao css-16my406 r-poiln3 r-b88u0q r-bcqeeo r-qvutc0']").text
    except:
        retweets = None
    try:
        quote = driver.find_element_by_xpath("//html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[4]/div/div[2]/div/a/div/span/span/span").text
    except:
        pass
    try:
        likes = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[4]/div/div[3]/div/a/div/span/span/span").text
    except:
        likes = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[4]/div/div[2]/div/a/div/span/span/span").text
    
    with open(r"E:\my_projects\twitter2_datasheet.csv",'a',encoding='utf8') as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerow([keyword, url, description, username, retweets, quote, likes])
        continue
print("description over")
driver.close()
