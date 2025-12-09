# Dependent-Independent xpath
#     *   Identify the dependent-independent xpath
#     *   Write the xpath of the independent element
#     *   Traverse back(/..) until we get the common match for dependent-independent element
import time

# # Eg1. wap to click on the checkbox of Ruby in demo.html
#
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M15-Aug11\files_\demo.html')
# time.sleep(2)
# driver.find_element('xpath', '//td[text()="Ruby"]/..//input[@name="download"]').click()
#
# # ###############################################################################################
#
# #Eg2. wap to click on the download link of windows in demo.html
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M15-Aug11\files_\demo.html')
# time.sleep(2)
# driver.find_element('xpath', '//td[text()="Windows"]/..//a[text()="Download"]').click()
#
#
# ###############################################################################################
#
# #Eg3. wap to click on the release notes of python 3.13.4 in https://www.python.org/
#
# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.get('https://www.python.org/')
# time.sleep(2)
# #clicking on downloads
# driver.find_element('xpath', '(//a[text()="Downloads"])[1]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Python 3.13.4"]/../..//a[text()="Release Notes"]').click()
#
# ###############################################################################################
#
# #Eg4. wap to print the sellprice and buyprice of Gold in https://www.iforex.in/tools/live-rates
#
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# driver.get('https://www.iforex.in/tools/live-rates')
# time.sleep(4)
# gold_sellprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[2]')
# print(gold_sellprice)       ## web-element
# print(f"Sell price of Gold is {gold_sellprice.text}")
# gold_buyprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[3]')
# print(f"Buy price of Gold is {gold_buyprice.text}")


###############################################################################################

#Eg5. wap to print the price of Tatamotors in https://in.tradingview.com/

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

driver.get('https://in.tradingview.com/')
time.sleep(2)
driver.find_element('xpath', '//span[text()="Search"]').click()
time.sleep(2)
driver.find_element('xpath', '//input[@name="query"]').send_keys('HAL')
time.sleep(2)
driver.find_element('xpath', '(//button[@aria-label="Search"])[3]').click()
time.sleep(2)

hal = driver.find_element('xpath', '//span[text()="HAL"]/../../..//span[@class="priceWrapper-qWcO4bp9"]')
print(hal.text)