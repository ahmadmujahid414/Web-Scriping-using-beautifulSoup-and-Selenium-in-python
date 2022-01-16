import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import requests




#path of the chromedriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
#pass the chromedriver path into the chrome so webdriver get access
browser = webdriver.Chrome(PATH)
browser.get("https://www.edmunds.com/cars-for-sale-by-owner/")

def search_postalCode(P_code):
    
    postalCode_box = browser.find_element_by_name("zip")
    #In the next line  to clear the text field 
    #because there is present a default value
    #which is 09622
    postalCode_box.send_keys(Keys.CONTROL + "a")
    postalCode_box.send_keys(Keys.DELETE)
    #after clearing the field it will wait 3 second
    #to execute next command 
    time.sleep(3)
    postalCode_box.send_keys(P_code)
    postalCode_box.send_keys(Keys.RETURN)



def search_radius(radius):
#here you can see on the left side there are some values
# which is used in  program to get the seach result the 
# user from radius
#-100 = 10miles
#-50 = 25miles
#-30 = 50miles
#0 = 75miles
#30 = 100miles
#50 = 200 miles
#100 = 500miles
    switcher = {"10":"-100",                   
                "25":"-50",
                "50":"-30",
                "75": "0",
                "100":"30",
                "200":"50",
                "500":"100"}
                   
    elem1 = browser.find_element(By.XPATH, "//input[contains(@class,'top-slider')]")
    ac = ActionChains(browser).click_and_hold(elem1)
    ac.pause(1)
    ac.move_by_offset(switcher.get(radius),0)
    ac.release().perform()

def website_content():
    return browser.page_source
def quit():
    browser.quit()

def show_cars(link_text):
    link = browser.find_element_by_link_text(link_text)
    link.click()
def back_to_main_page():
    browser.back()