import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    """Set up the WebDriver for Selenium."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode for testing
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def test_table_search():
    driver = setup_driver()
    try:
        url = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
        driver.get(url)

        # Use explicit wait to locate the search box
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "task-table-filter"))
        )
        search_box.send_keys("New York")

        # Wait for the rows to be updated after filtering
        WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, "//table[@id='task-table']/tbody/tr[not(contains(@style, 'display: none'))]"))
        )

        # Validate the search results
        rows = driver.find_elements(By.XPATH, "//table[@id='task-table']/tbody/tr[not(contains(@style, 'display: none'))]")
        assert len(rows) == 5, f"Expected 5 entries, but found {len(rows)}."

        # Wait for the total rows to load as well
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//table[@id='task-table']/tbody/tr"))
        )
        total_rows = driver.find_elements(By.XPATH, "//table[@id='task-table']/tbody/tr")
        assert len(total_rows) == 24, f"Expected 24 total entries, but found {len(total_rows)}."

    finally:
        driver.quit()

