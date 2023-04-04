# Python code using the Selenium library to automate the process of searching for and filtering products on the MercadoLibre website #
# Wrote by: @viclop

# Import necessary modules from the Selenium library:
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function that receives a parameter for the desired waiting time and call it every time you need to wait
# It helps to avoid the use of time.sleep() and make the code more readable. 
# Also it helps to avoid the use of implicit waits and let the page load completely.
def wait(seconds):
    time.sleep(seconds)

# Set up the Selenium driver in detached mode and maximize the window:
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Wait for 2 seconds
wait(2)

# Navigate to the MercadoLibre website
driver.implicitly_wait(10)
driver.get("https://www.mercadolibre.com")
print("Navigated to MercadoLibre website.")

wait(2)

# Click on the mexican flag 
driver.find_element(By.CSS_SELECTOR, "#MX").click()

wait(2)

# Click on the "Más tarde" on aking for location
WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div[2]/button[2]/span"))).click()

wait(2)

# Type "playstation 4" in the search bar
search_box = driver.find_element(By.CSS_SELECTOR, "#cb1-edit")
search_box.send_keys("Playstation 4")
search_box.send_keys(Keys.RETURN)

wait(2)

# quit the ookies
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div[2]/button[1]"))).click()

wait(2)

# Filter by "Nuevos"
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[2]/aside/section/div[7]/ul/li[1]/a/span[1]"))).click()

wait(2)

# Filter by location "Cdmx"
driver.find_element(By.XPATH, "/html/body/main/div/div[2]/aside/section[2]/div[14]/ul/li[1]/a/span[1]").click()

wait(2)

# Order by "mayor a menor precio"
driver.find_element(By.CSS_SELECTOR, ".andes-dropdown__display-values").click()
driver.find_element(By.CSS_SELECTOR, "#andes-dropdown-más-relevantes-list-option-price_desc > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)").click()

wait(2)

# Obtain the name and the price of the first 5 products
products_name = driver.find_elements(By.CSS_SELECTOR, ".ui-search-item__title")
products_price = driver.find_elements(By.CSS_SELECTOR, ".price-tag .price-tag-symbol + .price-tag-fraction:not(.ui-search-installments .price-tag-fraction)")
 #just take the price of the product and not the monthly payment

wait(2)

# Create an empty list
product_info = []

# Check if there are at least 5 products in the list and if so, add the name and price of the first 5 products to the list
if len(products_name) < 5 or len(products_price) < 5:
    print("There are less than 5 products in the list.")
else:
    for i in range(5):
        product_info.append(f"Product Name: {products_name[i].text}\nPrice: ${products_price[i].text}\n")

# Print the list
print("\nHere is the name and price of the first 5 products order by mayor a menor precio:\n")
for info in product_info:
    print(info)
    
# Close the browser # this quit the driver instance after the test completes
driver.quit()
print("Final of the test.")