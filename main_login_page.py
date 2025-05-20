# selenium_test.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Example: Initialize WebDriver and navigate to a page
driver = webdriver.Chrome()
# Make sure you have the ChromeDriver in your PATH
driver.get("https://www.fb.com")
# Example action
print("Page title is:", driver.title)
el_1 = driver.find_element(By.XPATH,"")
el_1.send_keys("asdfghjk")
time.sleep(2)
el_2 = driver.find_element(By.XPATH,"")
el_2.send_keys("asdfghjk")
time.sleep(2)
el_3 = driver.find_element(By.XPATH,"")
el_3.click()
time.sleep(5)
# Close the browser
driver.quit()






