Selenium Pytest Table Search Automation
Overview
This project automates table search functionality testing using Selenium and Pytest. It navigates to a demo table, searches for 'New York,' and verifies the search results.
Prerequisites
Ensure you have the following installed:
•	Python (>=3.7)
•	Google Chrome
•	ChromeDriver (Managed automatically by webdriver-manager)
•	Required Python packages (see Installation section)
Installation
1.	Clone the repository: 
2.	git clone <repository_url>
3.	cd <repository_folder>
4.	Create a virtual environment (optional but recommended): 
5.	python -m venv venv
6.	source venv/bin/activate  # On Windows: venv\Scripts\activate
7.	Install dependencies: 
8.	pip install -r requirements.txt
Running the Test
Execute the test using:
pytest -v --capture=no
Test Details
•	Navigates to the LambdaTest table page
•	Searches for 'New York' in the table
•	Extracts and validates search results
File Structure
.
├── test_table_search.py  # Selenium test script
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
Troubleshooting
•	Ensure Chrome is up-to-date or manually install ChromeDriver if issues arise.
•	Remove --headless in ChromeOptions for debugging.


