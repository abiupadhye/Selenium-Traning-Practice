import time

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get("https://www.apple.com/in/")
driver.maximize_window()
time.sleep(2)
driver.find_element("link text","Mac").click()

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get("https://www.udemy.com/?srsltid=AfmBOoo4hmoNb6Wh5YORtxfUokZWS5Ey9-BzMF4T4xB4IKtxnPsFrA_F")
time.sleep(3)
driver.find_element("link text","Sign up").click()
time.sleep(3)
driver.find_element("name","full-name").send_keys("Pookie")
time.sleep(3)
driver.find_element("name","email").send_keys("Pookie@gmail.com")
time.sleep(3)
driver.find_element("class name","ud-icon.ud-icon-xsmall.ud-fake-toggle-input.ud-fake-toggle-checkbox").click()
time.sleep(3)
driver.find_element("class name","ud-btn.ud-btn-large.ud-btn-brand.ud-btn-text-md.passwordless-auth-mx-code-generation-form--submit-button--2vOvZ").click()