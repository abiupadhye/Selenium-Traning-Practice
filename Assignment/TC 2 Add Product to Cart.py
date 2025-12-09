# Precondition: User must be logged in
# Test Steps
# 1. Login to application
# 2. Select a product (e.g., Nokia lumia 1520) from home page
# 3. Click Add to Cart
# Expected Result: Product added Message should be dissplyed.

import time

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element('xpath',"//a[text()='Log in']").click()
time.sleep(2)
driver.find_element('xpath',"//input[@id='loginusername']").send_keys('abi_upadhye')
time.sleep(2)
driver.find_element('xpath',"//input[@id='loginpassword']").send_keys('Upadhye@98')
time.sleep(2)
driver.find_element('xpath',"//button[text()='Log in']").click()
time.sleep(5)
driver.find_element('xpath',"//a[text()='Nokia lumia 1520']").click()
time.sleep(2)
driver.find_element('xpath',"//a[text()='Add to cart']").click()