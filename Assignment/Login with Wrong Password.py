# Steps	Enter valid username but invalid password → Login
# Expected Result	Alert popup should display: "Wrong password." and user should not login
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
driver.find_element('xpath',"//input[@id='loginpassword']").send_keys('Upadhye@97')
time.sleep(2)
driver.find_element('xpath',"//button[text()='Log in']").click()
