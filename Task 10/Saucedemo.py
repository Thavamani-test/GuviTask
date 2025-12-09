from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Initialising Chrome Webdriver
driver = webdriver.Chrome()

#Visit the URL using get
driver.get("https://www.saucedemo.com/")
time.sleep(2)

#Login using Credentials
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "input[class='submit-button btn_action']").click()
time.sleep(3)

#Fetch the title of the Webpage
title = driver.title
print("Title of the Webpage : ", title)

#Fetch current URL of the Webpage
current_url = driver.current_url
print("Current URL of the Webpage : ", current_url)

#Extract the entire Webpage contents
page_source = driver.page_source

#Save the content into a text file
with open("Webpage_task_10.txt", "w", encoding="utf-8") as file:
    file.write(page_source)

print("Webpage content saved to Webpage_task_10.txt")
