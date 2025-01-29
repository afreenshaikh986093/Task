Selenium Pytest Table Search Automation

Overview

This project automates the testing of a sortable and searchable table using Selenium and Pytest. The script navigates to a sample table on LambdaTest, searches for a keyword, and verifies the expected results.

Prerequisites

Ensure you have the following installed:

Python (>=3.7)

Google Chrome

ChromeDriver (Managed automatically by webdriver-manager)

Required Python packages (see Installation section)

Installation

Clone the repository:

git clone <repository_url>
cd <repository_folder>

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Running the Test

Execute the test using:

pytest -v --capture=no

Test Details

Navigates to the LambdaTest table page

Searches for 'New York' in the table

Verifies that relevant search results are displayed

File Structure

.
├── test_table_search.py  # Main Selenium test script
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation

Troubleshooting

If ChromeDriver issues arise, ensure Chrome is up-to-date or manually install ChromeDriver.

Run without headless mode for debugging by removing --headless from ChromeOptions.





