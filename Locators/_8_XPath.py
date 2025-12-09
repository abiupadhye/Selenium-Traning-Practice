import time

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()
time.sleep(2)

#Absoulte Xpath
driver.find_element('xpath','html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a').click()
time.sleep(2)

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(2)
driver.find_element('xpath', "html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div/input").send_keys('OnePlus Mobile')
time.sleep(2)



