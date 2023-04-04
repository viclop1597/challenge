import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service

#run with $ pytest -s test2.py para ver los prints 

@pytest.fixture(scope="module")
def browser():
    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_select_mexico(browser):
    # define the function that wraps the original code
    def select_mexico(driver):
        # Navigate to the website
        driver.get("https://www.mercadolibre.com")
        print("Navigated to MercadoLibre website.")

        # Wait for the page to load
        time.sleep(5)

        try:
            # Wait for the country selector element to be visible
            country_selector = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@id='country-button']"))
            )

            # Click on the country selector element
            country_selector.click()

            # Wait for the list of countries to be visible
            country_list = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "ml-site-list"))
            )

            # Find the "Mexico" option in the list and click on it
            mexico_option = country_list.find_element_by_xpath("//a[@id='MX']")
            mexico_option.click()

            # Verify that the website now displays the "México" text
            mexico_text = WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "ml-site-link"), "México")
            )
            print("Verified that the selected country is now Mexico.")

        except TimeoutException as ex:
            print(f"Timeout occurred: {ex}")
    
    # call the function inside the test function
    select_mexico(browser)
