from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless") 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://example.com/")

try:
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "html")))

    page_source = driver.page_source
    with open("page.html", "w", encoding="utf-8") as f:
        f.write(page_source)

    print("Saved as page.html")

except Exception as e:
    print("Błąd:", e)

finally:
    driver.quit()
