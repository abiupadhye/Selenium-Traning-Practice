import time

from selenium import webdriver
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.TAG_NAME,"a").click()
driver.find_elements(By.TAG_NAME, "a")[2].click()
time.sleep(1)

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element('partial link text','Create new').click()
time.sleep(1)
driver.find_element('name','firstname').send_keys('Abhishek')
time.sleep(1)
driver.find_element('name','lastname').send_keys('Upadhye')
time.sleep(1)
driver.find_element('css selector',"input[value='2']").click()
time.sleep(1)
driver.find_element('name','reg_email__').send_keys('7204071689')
time.sleep(1)
driver.find_element('name','reg_passwd__').send_keys('Abhishek@98')
time.sleep(1)
driver.find_element('partial link text','Sign Up').click()


