from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("almonds")
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").clear()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("lon")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
items = len(results)
assert items > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()                                                                  
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
time.sleep(3)
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

dropDown = Select(driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div/div/select"))
dropDown.select_by_value("United Kingdom")
time.sleep(2)
driver.find_element(By.CLASS_NAME, "chkAgree").click()  
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
time.sleep(5)

driver.close()


