import pytest
from selenium import webdriver

@pytest.fixture
def start_sauce() :
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    return driver
