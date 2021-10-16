import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.keys import Keys
import pyautogui

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("https://www.facebook.com/")
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("pass").clear()
driver.find_element_by_name("pass").send_keys("password")
driver.find_element_by_name("login").click()
pyautogui.click(332, 186)
driver.get("link wher you want to react wow")
time.sleep(4)
pyautogui.click(332, 186)
keyboard = Controller();
for i in range(0, 10): #can set range for how many posts we want to react
    time.sleep(5)
    pyautogui.press('j')
    time.sleep(1)
    pyautogui.press("l")
    time.sleep(1)
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('tab')  
    time.sleep(1)
    pyautogui.press('enter')
        

driver.close()