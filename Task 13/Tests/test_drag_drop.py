import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    InvalidSelectorException,
    WebDriverException
)

#Positive Test Case
def test_drag_drop_positive(start_browser):
    try:
        #launch an url
        start_browser.get("https://jqueryui.com/droppable/")
        wait = WebDriverWait(start_browser, 10)

        #switch to iframe
        iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='demo-frame']")))
        start_browser.switch_to.frame(iframe)

        source = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'ui-draggable')]")))
        target = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'ui-droppable')]")))

        actions = ActionChains(start_browser)
        actions.drag_and_drop(source, target).perform()

        # Validation
        assert "Dropped!" in target.text
        print("Positive Test Passed: Drag and Drop Successful")

    except (TimeoutException, NoSuchElementException, InvalidSelectorException) as e:
        start_browser.save_screenshot("positive_test_failure.png")
        pytest.fail(f"Positive Test Failed due to Selenium issue: {e}")

    except AssertionError as e:
        start_browser.save_screenshot("positive_assertion_failure.png")
        pytest.fail(f"Positive Test Assertion Failed: {e}")

    except WebDriverException as e:
        pytest.fail(f"WebDriver Error occurred: {e}")

#Negative Test Case
def test_drag_drop_negative(start_browser):
    try:
        # launch an url
        start_browser.get("https://jqueryui.com/droppable/")
        wait = WebDriverWait(start_browser, 10)

        # switch to iframe
        iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='demo-frame']")))
        start_browser.switch_to.frame(iframe)

        target = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'ui-droppable')]")))

        # No drag action done
        assert "Dropped!" not in target.text
        print("Negative Test Passed: No Drag Action Performed")

    except (TimeoutException, NoSuchElementException, InvalidSelectorException) as e:
        start_browser.save_screenshot("negative_test_failure.png")
        pytest.fail(f"Negative Test Failed due to Selenium issue: {e}")

    except AssertionError as e:
        start_browser.save_screenshot("negative_assertion_failure.png")
        pytest.fail(f"Negative Test Assertion Failed: {e}")

    except WebDriverException as e:
        pytest.fail(f"WebDriver Error occurred: {e}")
