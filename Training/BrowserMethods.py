import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

# LAUNCH THE APPLICATION
driver.get('https://www.myntra.com/')
time.sleep(2)

driver.maximize_window()
time.sleep(2)

# MINIMIZE BROWSER
#driver.minimize_window()
#time.sleep(2)

# TO BACK
driver.back()
time.sleep(2)

# TO GO FORWARD
driver.forward()
time.sleep(2)

# TO REFRESH
driver.refresh()
time.sleep(2)

# PROPERTIES
print(driver.current_url)
print(driver.title)
print(driver.name)
#print(driver.page_source)

# TO TAKE THE SCREENSHOTS
#driver.save_screenshot('myntra_homepage.png')

driver.save_screenshot(r'C:\Users\Abhishek\PycharmProjects\Selenium_Training\Files\myntra_homepage.png')

# TO CLOSE THE BROWSER
driver.close()

from selenium import webdriver
opts = webdriver.EdgeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Edge(opts)
driver.get('https://www.amazon.in/')
time.sleep(2)
driver.maximize_window()
time.sleep(2)
#driver.minimize_window()
#time.sleep(2)
driver.back()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
print(driver.current_url)
print(driver.title)
print(driver.name)
#print(driver.page_source)
driver.save_screenshot(r'C:\Users\Abhishek\PycharmProjects\Selenium_Training\Files\amazon_homepage.png')
driver.close()

from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.flipkart.com/')
time.sleep(2)
driver.maximize_window()
time.sleep(2)
#driver.minimize_window()
#time.sleep(2)
driver.back()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
print(driver.current_url)
print(driver.title)
print(driver.name)
#print(driver.page_source)
driver.save_screenshot(r'C:\Users\Abhishek\PycharmProjects\Selenium_Training\Files\flipkart_homepage.png')
driver.close()