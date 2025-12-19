import time
from selenium import webdriver
from selenium.webdriver.common.by import By


#Initialising Chrome Webdriver
driver = webdriver.Chrome()

#Visit the URL using get
driver.get("https://www.guvi.in/")
driver.maximize_window()
time.sleep(2)
#Login Button migration to Signup page
#driver.find_element(By.CSS_SELECTOR, "button.tertiary-btn").click()
driver.find_element(By.XPATH, "//button[contains(@class,'tertiary-btn')]").click()
print("Current URL of the Webpage : ", driver.current_url)

#Login using Credentials
driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("thavamani.ravindran@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("Profession@four4")
driver.find_element(By.XPATH, "//a[@class='btn login-btn']").click()
time.sleep(2)

print("Logged in Successfully")