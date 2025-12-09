# Precondition: Product must be added to cart
# Test Steps:
# 1. Go to Cart page
# 2. Click Place Order
# 3. Enter required details (Name, Country, City, Card)
# 4. Click Purchase
# 5. Confirm success message
# Expected Result: Purchase success popup should appear with transaction ID and amount
import time

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
time.sleep(2)

driver.find_element('xpath',"//a[text()='Cart']").click()
time.sleep(2)
driver.find_element('xpath',"//button[text()='Place Order']").click()
time.sleep(2)
driver.find_element('xpath',"//input[@id='name']").send_keys('Abhishek Upadhye')
time.sleep(2)
driver.find_element('xpath',"//input[@id='country']").send_keys('India')
time.sleep(2)
driver.find_element('xpath',"//input[@id='city']").send_keys('Bangalore')
time.sleep(2)
driver.find_element('xpath',"//input[@id='card']").send_keys('121214565625')
time.sleep(2)
driver.find_element('xpath',"//input[@id='month']").send_keys('November')
time.sleep(2)
driver.find_element('xpath',"//input[@id='year']").send_keys('11')
time.sleep(2)
driver.find_element('xpath',"//button[text()='Purchase']").click()
time.sleep(2)
driver.find_element('xpath',"//button[text()='OK']").click()
time.sleep(2)




