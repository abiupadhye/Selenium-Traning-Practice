# Precondition: User must be logged in
# Test Steps:
# 1. Login to application
# 2. Select a product (e.g., Samsung S6) from home page
# 3. Click Add to Cart
# 4. Accept alert pop-up
# 5. Navigate to Cart page
# Expected Result: Product should be visible in the cart list

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

