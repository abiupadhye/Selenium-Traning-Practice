import time

#AMAZON EXAMPLE
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element("xpath","//input[@id='twotabsearchtextbox']").send_keys("OnePlus Mobile")
# time.sleep(2)
# driver.find_element("xpath","//input[@id='nav-search-submit-button']").click()
#
# # EXAMPLE
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element("xpath","//a[@class='ico-register']").click()
# time.sleep(2)
# driver.find_element("xpath","//input[@id='gender-male']").click()
# time.sleep(2)
# driver.find_element("xpath","//input[@id='FirstName']").send_keys("Abhishek")
# time.sleep(2)
# driver.find_element("xpath","//input[@id='LastName']").send_keys("Upadhye")
# time.sleep(2)
# driver.find_element("xpath","//input[@id='Email']").send_keys("abhishekupadhye21@gmail.com")
# time.sleep(2)
# driver.find_element("xpath","//input[@id='Password']").send_keys("Upadhye@98")
# time.sleep(2)
# driver.find_element("xpath","//input[@id='ConfirmPassword']").send_keys("Upadhye@98")
# time.sleep(2)
# driver.find_element("xpath","//input[@id='register-button']").click()
# time.sleep(2)
# driver.find_element("xpath","//input[@class='button-1 register-continue-button']").click()
# time.sleep(2)
# driver.find_element("xpath","//a[@class='ico-logout']").click()
# time.sleep(2)
# driver.find_element("xpath","//a[@class='ico-login']").click()
# time.sleep(2)
# driver.find_element("xpath","//input[@id='Email']").send_keys("abhishekupadhye21@gmail.com")
# time.sleep(2)
# driver.find_element("xpath","//input[@id='Password']").send_keys("Upadhye@98")
# time.sleep(2)
# driver.find_element("xpath","//input[@class='button-1 login-button']").click()
# time.sleep(2)
#
#
# # Text Example
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element("xpath","//button[text()='Continue shopping']").click()
# time.sleep(3)
# driver.find_element("xpath",'''//a[text()="Today's Deals"]''').click()
# time.sleep(3)
# driver.find_element(by="xpath", value="//button[text()='Coupons']").click()
# time.sleep(3)
# driver.find_element(by="xpath", value="//span[text()='Appliances']").click()
# time.sleep(3)
# driver.find_element(by="xpath", value="//a[text()='Clear Filters']").click()
#
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# driver.get("https://blinkit.com/")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element(by='xpath',value="//button[text()='Detect my location']").click()
# time.sleep(3)
# driver.find_element(by='xpath',value="//div[text()='Login']").click()
# time.sleep(3)
# driver.find_element(by='xpath',value="//input[@class='login-phone__input input']").send_keys('7204071689')
# time.sleep(3)
# driver.find_element('xpath',"//button[text()='Continue']").click()

#INDEX EXAMPLE
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get("https://www.facebook.com/r.php?entry_point=login")
driver.maximize_window()
time.sleep(3)
driver.find_element('xpath','(//input[@type="text"])[1]').send_keys('Abhishek')
time.sleep(3)
driver.find_element('xpath','(//input[@type="text"])[2]').send_keys('Upadhye')


























