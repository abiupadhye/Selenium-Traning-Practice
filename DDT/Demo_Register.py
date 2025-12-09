import time

from selenium import webdriver
from DDT.Read_Excel import reading_testdata

path = r'C:\Users\Abhishek\PycharmProjects\Selenium_Training\DDT\Demo_TestData.xlsx'
data = reading_testdata(path, sheetname='register')

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

driver.find_element('xpath','//a[text()="Register"]').click()
time.sleep(1)
driver.find_element('xpath','//input[@id="gender-male"]').click()
driver.find_element('xpath','//input[@id="FirstName"]').send_keys(data['firstname'])
driver.find_element('xpath','//input[@id="LastName"]').send_keys(data['lastname'])
driver.find_element('xpath','//input[@id="Email"]').send_keys(data['email_id'])
driver.find_element('xpath','//input[@id="Password"]').send_keys(data['pwd'])
driver.find_element('xpath','//input[@id="ConfirmPassword"]').send_keys(data['confirm_pwd'])
driver.find_element('xpath','//input[@id="register-button"]').click()

















































































