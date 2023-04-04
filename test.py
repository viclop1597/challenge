import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    # Set up the Chrome browser
    # Path to the Chrome driver executable
    chrome_driver_path = '/usr/local/bin/chromedriver'
    # Create a Chrome driver service instance with the specified path
    service = Service(executable_path=chrome_driver_path)
    # Create a Chrome driver instance with the specified service
    driver = webdriver.Chrome(service=service)
    yield driver
    # Tear down the browser after the test
    driver.quit()




def test_search_ps4(browser):

    # Navigate to the MercadoLibre website
    browser.get('https://www.mercadolibre.com/')
    print("Navigated to MercadoLibre website.")

    # Wait for the select element to be visible
    select_locator = (By.XPATH, '//select[@name="id"]')
    wait = WebDriverWait(browser, 30)
    select_element = wait.until(EC.visibility_of_element_located(select_locator))

    # Create a Select object for the element
    select = Select(select_element)

    # Select "México" from the dropdown menu
    select.select_by_visible_text('México')