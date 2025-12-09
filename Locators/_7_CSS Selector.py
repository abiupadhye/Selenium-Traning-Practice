import time

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()
time.sleep(2)
driver.find_element("css selector","input[class='email']").send_keys("amitabhbachhan@gmail.com")

