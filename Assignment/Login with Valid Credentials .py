# Precondition: The username being used should not already exist in the system
# Test Steps
# 1. Open the Demoblaze website
# 2. Click on Sign up in the top menu
# 3. Enter Username in the username input field
# 4. Enter Password in the password input field
# 5. Click on Sign up button
# Expected Result: A popup should appear saying "Sign up successful." and the user should be registered successfully.

import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element('xpath',"//a[text()='Sign up']").click()
time.sleep(2)
driver.find_element('xpath',"//input[@id='sign-username']").send_keys('abii_upadhye')
time.sleep(2)
driver.find_element('xpath',"//input[@id='sign-password']").send_keys('Upadhye@98')
time.sleep(2)
driver.find_element('xpath',"//button[text()='Sign up']").click()
time.sleep(2)


