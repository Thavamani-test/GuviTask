import time
from selenium.webdriver.common.by import By

#Positive Test Cases
def test_title_positive(start_sauce) :
    start_sauce.get("https://www.saucedemo.com/")
    time.sleep(2)
    assert start_sauce.title == "Swag Labs"

def test_url_homepage_positive(start_sauce) :
    start_sauce.get("https://www.saucedemo.com/")
    time.sleep(2)
    assert start_sauce.current_url == "https://www.saucedemo.com/"

def test_dashboard_url_positive(start_sauce) :
    start_sauce.get("https://www.saucedemo.com/")
    start_sauce.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys("standard_user")
    start_sauce.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("secret_sauce")
    start_sauce.find_element(By.CSS_SELECTOR, "input[class='submit-button btn_action']").click()
    time.sleep(2)

    assert "inventory.html" in start_sauce.current_url


#Negative Test Cases
def test_wrong_title_negative(start_sauce) :
    start_sauce.get("https://www.saucedemo.com/")
    time.sleep(2)
    assert start_sauce.title != "Wrong Title"

def test_wrong_url_homepage_negative(start_sauce) :
    start_sauce.get("https://www.saucedemo.com/")
    time.sleep(2)
    assert start_sauce.current_url != "https://www.fakeurl.com/"

def test_login_invalid_username_negative(start_sauce) :
    start_sauce.get("https://www.saucedemo.com/")
    start_sauce.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys("new_user")
    start_sauce.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("secret_sauce")
    start_sauce.find_element(By.CSS_SELECTOR, "input[class='submit-button btn_action']").click()

    error_msg = start_sauce.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "Username and password do not match any user in this service" or "Epic sadface" in error_msg
    time.sleep(2)

def test_login_invalid_password_negative(start_sauce):
        start_sauce.get("https://www.saucedemo.com/")
        start_sauce.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys("standard_user")
        start_sauce.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("new_pwd")
        start_sauce.find_element(By.CSS_SELECTOR, "input[class='submit-button btn_action']").click()

        error_msg = start_sauce.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        assert "Username and password do not match any user in this service" or "Epic sadface" in error_msg

        time.sleep(2)
        start_sauce.quit()