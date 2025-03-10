from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Setup Selenium WebDriver
options = Options()
options.add_argument("--headless")  # Runs in the background
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Base URL for pagination
base_url = "https://www.tncenturyfarms.org/farms/?listpage={}&instance=1"

# Initialize Data List
farm_data = []
total_farms_scraped = 0
max_farms = 2150  # Total expected farms
farms_per_page = 10
total_pages = max_farms // farms_per_page  # Approximate number of pages

# Loop through each page directly using URLs
for page_num in range(1, total_pages + 1):
    print(f"Scraping page {page_num}...")

    # Load the specific page URL
    driver.get(base_url.format(page_num))
    time.sleep(3)  # Wait for page to load

    # Get all rows in the table
    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

    # Scrape farms from this page
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        farm = [col.text.strip() for col in cols]
        if farm and farm not in farm_data:
            farm_data.append(farm)
            total_farms_scraped += 1

    print(f"Total farms scraped so far: {total_farms_scraped}")

    # Stop if we reach the total expected farms
    if total_farms_scraped >= max_farms:
        break

# Save data to CSV
df = pd.DataFrame(farm_data, columns=["Farm Name", "County", "Date Founded", "Special Recognition"])
df.to_csv("century_farms.csv", index=False, encoding="utf-8")

print("Scraping complete. Data saved to century_farms.csv")
driver.quit()
