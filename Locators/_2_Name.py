import time

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get("https://www.instagram.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element('name','username').send_keys('abi_upadhye')
time.sleep(1)
driver.find_element('name','password').send_keys('Upadhye@1998')


from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get("https://www.facebook.com/r.php?entry_point=login")
driver.maximize_window()
time.sleep(2)
driver.find_element('name','firstname').send_keys('Abhishek')
time.sleep(1)
driver.find_element('name','lastname').send_keys('Upadhye')
time.sleep(1)
driver.find_element('name','reg_email__').send_keys('7204071689')
time.sleep(1)
driver.find_element('name','reg_passwd__').send_keys('Upadhye@9879')

