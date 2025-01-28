
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (this assumes you have chromedriver in your PATH)
driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://www.google.com")

# Find the search box and search for "Selenium"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds to see the results
time.sleep(5)

# Close the browser
driver.quit()
