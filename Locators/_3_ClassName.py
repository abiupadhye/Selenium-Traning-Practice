import time

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()

driver.find_element("class name", "text-box.single-line").send_keys("abi_upadhye")
time.sleep(1)
driver.find_element("class name", "text-box.single-line").click()
time.sleep(1)