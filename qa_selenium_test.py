import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup function to initialize WebDriver
def setup_driver():
    """Set up the WebDriver for Selenium."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode for testing
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# Test function to search the table and validate the results
def test_table_search():
    # Initialize WebDriver
    driver = setup_driver()
    try:
        # Base URL and search query
        baseURL = 'https://www.lambdatest.com/selenium-playground/table-sort-search-demo'
        mysearchKey = 'New York'
        # Navigate to the URL
        driver.get(baseURL)
        # Wait for the search box to be present on the page before interacting with it
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="example_filter"]/label/input')))
        # Find the search input element, clear any previous input, and enter the search query
        search_box.clear()
        search_box.send_keys(mysearchKey)  # Enter search term (e.g., 'New York')
        search_box.send_keys(Keys.RETURN)  # Press Enter to submit the search
        # Wait for the table rows to be updated based on the search query
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="example"]/tbody/tr')))
        # Extract data from the table rows after the search is applied
        rows = driver.find_elements(By.XPATH, '//*[@id="example"]/tbody/tr')
        # Create a list to store the extracted data from the table rows
        row_data = []
        for row in rows:
            name = row.find_element(By.XPATH, './td[1]').text
            position = row.find_element(By.XPATH, './td[2]').text
            office = row.find_element(By.XPATH, './td[3]').text
            age = row.find_element(By.XPATH, './td[4]').text
            row_data.append((name, position, office, age))
        # Print the extracted data from the table
        for data in row_data:
            print(f"Name: {data[0]}, Position: {data[1]}, Office: {data[2]}, Age: {data[3]}")
        # Assertions to validate that the results are as expected
        # Assert that at least one row is found after the search
        assert len(rows) > 0, "No rows found after searching for 'New York'"
        # Assert that 'New York' appears in the office column in the extracted data
        assert any('New York' in row[2] for row in row_data), "'New York' not found in office column"
    finally:
        # Close the browser when done
        driver.quit()
        
# The main function to run the test script directly
if __name__ == "__main__":
    pytest.main(["-v", "--capture=no", __file__])  # Run the pytest with the current script
