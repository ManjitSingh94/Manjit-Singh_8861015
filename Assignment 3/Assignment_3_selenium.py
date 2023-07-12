# Importing required libraries

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(4)

# Selecting electronics option from the product categories in homepage
electronic_link = driver.find_element("xpath","/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[6]")
electronic_link.click()
time.sleep(2)

# Selecting Cameras option from electronics types
cameras_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/ul[1]/li[7]/a")
cameras_link.click()
time.sleep(2)

# Selecting Digital Cameras from type of prdoucts available related to cameras
digicamera_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[2]/span/span/div/a/div[1]/div")
digicamera_link.click()
time.sleep(2)

# Selecting a Digital Cameras from available cameras
canoncamera_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div[3]/div[3]/div/div[2]/div[2]/ul/li[1]/span/div/a/div/div")
canoncamera_link.click()
time.sleep(2)

# Selecting Camera style
cameratype_link = driver.find_element("xpath","/html/body/div[2]/div[2]/div[4]/div[4]/div[4]/div[23]/div[1]/div/form/div/ul/li[4]/span/div/span/span/span/button/div/div[1]")
cameratype_link.click()
time.sleep(2)

# clicking on Try Prime
try_prime_box = driver.find_element("xpath","/html/body/div[2]/div[2]/div[4]/div[4]/div[1]/div[2]/div/div/div[1]/label/input")
try_prime_box.click()

# Closing the webdriver
driver.close()