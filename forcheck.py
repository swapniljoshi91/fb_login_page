# selenium_test.py

import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Target URL
driver.get("https://nz.mether.info/")
print("Page title is:", driver.title)

# Wait for page to load
time.sleep(2)

# Collect all links
links = driver.find_elements(By.TAG_NAME, "a")
print(f"Total links found: {len(links)}")

# Create an Excel workbook and sheet
wb = Workbook()
sheet = wb.active
sheet.title = "Link Test Results"
sheet.append(["S.No", "URL", "Status Code", "Result", "Description"])

# Check all links
count = 1
for link in links:
    url = link.get_attribute("href")

    # Skip if URL is None or invalid
    if not url or url.startswith("javascript"):
        sheet.append([count, url, "N/A", "Skipped", "No valid href or JavaScript link"])
        print(f"{url} : Skipped (No valid href or JavaScript link)")
        count += 1
        continue

    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        status_code = response.status_code
        if status_code >= 400:
            result = "Broken"
            description = "Link is broken or inaccessible"
        else:
            result = "Valid"
            description = "Link is working fine"
    except requests.exceptions.RequestException as e:
        status_code = "Error"
        result = "Failed"
        description = f"Request failed: {e}"

    sheet.append([count, url, status_code, result, description])
    print(f"{url} => {status_code} : {result} - {description}")
    count += 1
    time.sleep(1)  # Optional delay

# Save the Excel file
excel_filename = "job_link_test_results.xlsx"
wb.save(excel_filename)
print(f"\nResults saved to: {excel_filename}")

# Cleanup
driver.quit()