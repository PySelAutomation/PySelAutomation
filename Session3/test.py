import time

from test import webdriver
from test.webdriver.chrome.service import Service
from test.webdriver.common.by import By
from test.webdriver.support.select import Select

service_obj = Service("C:/Users/kaurm/Downloads/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://edwheel.com/index.php/selenium-practice/")

# Wait for the privacy dialog to appear (you might need to adjust the wait time)
driver.implicitly_wait(10)

# Find and click the "Reject All" button
try:
    reject_all_button = driver.find_element(By.XPATH, "(//button[contains(text(), 'Reject All')])[1]")
    reject_all_button.click()
    print("Clicked 'Reject All' button to dismiss privacy dialog.")
except Exception as e:
    print(f"Error: {e}")

# ID, xpath, cssselector, classname, name, linktext
driver.find_element(By.ID, "name").send_keys("Neelam Pal")
driver.find_element(By.NAME, "email").send_keys("support@edwheel.com")

# xpath - //tagname[@attribute='value'] -> //input[@type='submit']
# css - tagname[attribute='value] -> //in[ut[@type='submit]

# driver.find_element(By.CSS_SELECTOR)

time.sleep(10)
# dropdown = driver.find_element(By.XPATH("//select[@id='dropdown'']"))

# Create a Select object
# select = Select(dropdown)

# Select a value by visible text
# select.select_by_visible_text("DPValue 2")

# Alternatively, you can select a value by index (index starts from 0) or value attribute
# select.select_by_index(0)
# select.select_by_value("value_of_option_1")

driver.find_element(By.ID("chbValue1")).click()
