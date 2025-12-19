import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

#Positive Test Case
# Test Case-1 Validate the URL of the Login button
def test_valid_login_url_positive(start_browser):
        start_browser.get("https://www.guvi.in/")
        start_browser.implicitly_wait(5)
        start_browser.find_element(By.XPATH, "//button[contains(@class,'tertiary-btn')]").click()
        print("Current URL of the Webpage : ", start_browser.current_url)
        assert "https://www.guvi.in/sign-in/" in start_browser.current_url

# Test Case-2 Validate that the Username and Password input boxes are visible and enabled with the valid credentials
def test_input_boxes_visiblity_positive(start_browser):
        start_browser.get("https://www.guvi.in/sign-in/")
        start_browser.implicitly_wait(5)
        email = start_browser.find_element(By.CSS_SELECTOR, "input[type='email']")
        password = start_browser.find_element(By.CSS_SELECTOR, "input[type='password']")

        assert email.is_displayed() and email.is_enabled()
        assert password.is_displayed() and password.is_enabled()

        email.send_keys("thavamani.ravindran@gmail.com")
        password.send_keys("Profession@four4")

        email.clear()
        password.clear()

# Test Case-3 Validate that the Submit button is working properly
def test_submit_function_positive(start_browser):
        start_browser.get("https://www.guvi.in/sign-in/")
        start_browser.implicitly_wait(5)

        start_browser.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("thavamani.ravindran@gmail.com")
        start_browser.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("Profession@four4")
        start_browser.find_element(By.XPATH,"//a[@class='btn login-btn']").click()
        assert "sign-in" in start_browser.current_url


#Negative Test Case
# Test Case-1 Validate the URL with the Invalid Login Credentials
def test_invalid_login_credentials_negative(start_browser):
        start_browser.get("https://www.guvi.in/sign-in")
        start_browser.implicitly_wait(5)
        start_browser.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("abcd@gmail.com")
        start_browser.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("xyz@123")
        start_browser.find_element(By.XPATH, "//a[@class='btn login-btn']").click()

        #Showing Error message and
        error_msg = start_browser.find_element(By.XPATH, "//div[@class='invalid-feedback']")
        print("error message : ", error_msg)
        assert "Incorrect Email or Password" in error_msg.text

# Test Case-2 Validate that the Username and Password input boxes are not visible and not enabled
def test_input_boxes_visiblity_negative(start_browser):
        start_browser.get("https://www.guvi.in/sign-in/")
        start_browser.implicitly_wait(5)
        email = start_browser.find_element(By.CSS_SELECTOR, "input[type='email']")
        password = start_browser.find_element(By.CSS_SELECTOR, "input[type='password']")

        assert not (email.is_displayed() and email.is_enabled() is False)
        assert not (password.is_displayed() and password.is_enabled() is False)

        email.send_keys("thavamani.ravindran@gmail.com")
        password.send_keys("Profession@four4")

# Test Case-3
def test_submit_not_function_negative(start_browser):
        start_browser.get("https://www.guvi.in/sign-in/")
        start_browser.implicitly_wait(5)
        start_browser.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("abcd@gmail.com")
        start_browser.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("xyz@123")

        start_browser.find_element(By.XPATH, "//a[@class='btn login-btn']").click()
        assert "sign-in" in start_browser.current_url

