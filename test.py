from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium driver in detached mode
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Navigate to the MercadoLibre website
driver.implicitly_wait(10)
driver.get("https://www.mercadolibre.com")

# Click on the mexican flag
driver.find_element(By.CSS_SELECTOR, "#MX").click()

# Click on Más tarde
WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div[2]/button[2]/span"))).click()


# Type "playstation 4" in the search bar
search_box = driver.find_element(By.CSS_SELECTOR, "#cb1-edit")
search_box.send_keys("Playstation 4")
search_box.send_keys(Keys.RETURN)


# Filter by "Nuevos"
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div[2]/button[1]"))).click()
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[2]/aside/section/div[7]/ul/li[1]/a/span[1]"))).click()

# # Filter by location "Cdmx"
driver.find_element(By.XPATH, "/html/body/main/div/div[2]/aside/section[2]/div[14]/ul/li[1]/a/span[1]").click()

# # Order by "mayor a menor precio"
driver.find_element(By.CSS_SELECTOR, ".andes-dropdown__display-values").click()
driver.find_element(By.CSS_SELECTOR, "#andes-dropdown-más-relevantes-list-option-price_desc > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)").click()

# # Obtain the name and the price of the first 5 products
products_name = driver.find_elements(By.CSS_SELECTOR, ".ui-search-item__title")
products_price = driver.find_elements(By.CSS_SELECTOR, ".price-tag-fraction")

# # Print the name and price of the first 5 products
for i in range(5):
    print(f"Product Name: {products_name[i].text}\nPrice: ${products_price[i].text}\n")
    
# Close the browser
driver.quit()