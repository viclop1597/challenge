import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service

# run with $ pytest -s test2.py para ver los prints 

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

            # Find the list items in the country list
            country_items = country_list.find_elements(By.TAG_NAME, "li")

            # Loop through the list items and find the "Mexico" option
            for item in country_items:
                if item.text == "México":
                    mexico_option = item.find_element(By.TAG_NAME, "a")
                    mexico_option.click()
                    print("Clicked on the Mexico option.")
                    break

            # Verify that the website now displays the "México" text
            mexico_text = WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "ml-site-link"), "México")
            )
            print("Verified that the selected country is now Mexico.")

        except TimeoutException as ex:
            print(f"Timeout occurred: {ex}")
    
    # call the function inside the test function
    select_mexico(browser)
