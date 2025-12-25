import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_guvi_relative_xpath_axes(start_browser):

    # Initialising Chrome Webdriver
    start_browser = webdriver.Chrome()

    # Launching the URL
    start_browser.get("https://www.guvi.in/")
    start_browser.maximize_window()
    time.sleep(2)
    assert start_browser.current_url == "https://www.guvi.in/"

# Reference element (Courses)
    courses = start_browser.find_element(By.XPATH, "//p[contains(text(),'Courses')]")
    assert courses.is_displayed()

# Using Relative XPath
# Parent element
    parent = courses.find_element(By.XPATH, '..')
    assert parent is not None
    print(parent.tag_name)

# First child of the parent
    first_child = courses.find_element(By.XPATH, "../child::*[1]")
    assert first_child is not None
    print(first_child.tag_name)

# Second sibling
    second_sibling = courses.find_element(By.XPATH, "following-sibling::*[1]")
    assert second_sibling is not None
    print(second_sibling.tag_name)

# Parent element of an element with the attribute “href”
    href_element = start_browser.find_element(By.XPATH, "//*[@href][1]")
    href_parent = href_element.find_element(By.XPATH, "..")
    assert href_parent is not None
    print(href_parent.tag_name)

# Axes
# All ancestor elements
    ancestor = courses.find_elements(By.XPATH, "ancestor::*")
   # print(ancestor)
    assert len(ancestor) > 0
    print(len(ancestor))

# All following siblings
    following_siblings = courses.find_elements(By.XPATH, "following-sibling::*")
    assert len(following_siblings) >= 1
    print(len(following_siblings))

# All preceding elements
    preceding_elements = courses.find_elements(By.XPATH, "preceding::*")
    assert len(preceding_elements) > 0
    print(len(preceding_elements))

