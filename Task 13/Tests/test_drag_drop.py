from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

#Positive Test Case
def test_drag_drop_positive(start_browser):
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
    print("Dropped!")

#Negative Test Case
def test_drag_drop_negative(start_browser):
    # launch an url
    start_browser.get("https://jqueryui.com/droppable/")
    wait = WebDriverWait(start_browser, 10)

    # switch to iframe
    iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='demo-frame']")))
    start_browser.switch_to.frame(iframe)

    target = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'ui-droppable')]")))

    # No drag action done
    assert "Dropped!" not in target.text
    print("No Dragging done!")

