Selenium Web Scraper

Description
This script uses Selenium to open a webpage in headless Chrome, waits for the page to load, and saves the HTML source code to a file.

Requirements
Python 3.x
Google Chrome installed
ChromeDriver (managed automatically by webdriver-manager)

Installation
Clone this repository or download the script.
Install the required dependencies:
pip install selenium webdriver-manager

Usage
Run the script with:
python script.py

The script will:
Launch a headless Chrome browser.
Navigate to https://example.com/.
Wait for the page to load.
Save the page source to page.html.
Close the browser.

Error Handling
If an error occurs during execution, the script will print an error message and close the browser properly.

Customization
To scrape a different webpage, change the URL in:
driver.get("https://example.com/")
To modify waiting conditions, adjust the timeout value in:
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "html")))

License
This project is open-source and available under the MIT License.

