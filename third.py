
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

 
URL = "https://www.tripadvisor.in/Hotel_Review-g608486-d3167682-Reviews-Uppala_Villa_Seminyak-Kerobokan_Bali.html"

driver = webdriver.Chrome()  
driver.get(URL)


print("Starting to scrape...")

# click on the location button 

location = driver.find_element_by_xpath('//*[@id="TABS_LOCATION"]')
print(location)
location.click()
print("clicked")

driver.implicitly_wait(30)


#Once the page is loaded 

l = driver.find_element_by_xpath('//span[@class = "mapWxH"]/img')
driver.implicitly_wait(6)
data = l.get_attribute('src')
print(data)
print(type(data))

# Getting the latlong

fh = data.split("&center=")
print(fh)
p= fh[1].split("&maptype")
print(p[0])
