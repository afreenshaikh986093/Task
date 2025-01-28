import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    # Define the path to ChromeDriver using Service
    service = Service("C:\\Users\\hp\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_search(driver):    
    import pdb 
    pdb.set_trace()
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("pytest Selenium")
    search_box.submit()
    assert "pytest Selenium" in driver.title


    # Interact with the search box and search for "New York"
    search_box.clear()
    search_box.send_keys("New York")
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load and check the number of displayed entries
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".table tbody tr"))
    )

    # Get the rows displayed after search
    rows = driver.find_elements(By.CSS_SELECTOR, ".table tbody tr")
    
    # Validate that only 5 rows are shown out of 24
    assert len(rows) == 5, f"Expected 5 entries, but found {len(rows)} entries."

    # Check if total number of entries (in this case, the text is in the table)
    total_entries = driver.find_element(By.ID, "example_info").text
    assert "24" in total_entries, f"Expected '24 entries', but found: {total_entries}"

if __name__ == "__main__":
    
    pytest.main()
