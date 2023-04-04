import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def browser():
    # initialize the Chrome browser instance
    driver = webdriver.Chrome()
    driver.maximize_window()
    # yield the driver instance to the test method
    yield driver
    # quit the driver instance after the test completes
    driver.quit()

def test_select_mexico(browser):
    # Navigate to the MercadoLibre website
    browser.get('https://www.mercadolibre.com/')
    print("Navigated to MercadoLibre website.")
    
    # Wait for the select element to be visible
    select_locator = (By.CSS_SELECTOR, 'select[name="id_site"]')
    wait = WebDriverWait(browser, 30)
    select_element = wait.until(EC.visibility_of_element_located(select_locator))
    print("Found country selector element.")
    
    # Click on the select element to display the dropdown menu
    select_element.click()
    print("Clicked on country selector element.")
    
    # Find the Mexico option in the dropdown menu and click on it
    mexico_locator = (By.XPATH, '//li[@class="ml-site-mlm"]/a[@id="MX"]')
    mexico_element = wait.until(EC.element_to_be_clickable(mexico_locator))
    print("Found Mexico option in dropdown menu.")
    mexico_element.click()
    print("Clicked on Mexico option in dropdown menu.")
    
    # Verify that the selected country is now Mexico
    selected_country_locator = (By.CSS_SELECTOR, 'select[name="id_site"] option[selected="selected"]')
    selected_country_element = wait.until(EC.visibility_of_element_located(selected_country_locator))
    selected_country_name = selected_country_element.text
    assert selected_country_name == "México", f"Selected country is not Mexico: {selected_country_name}"
    print("Verified that the selected country is now Mexico.")