import time

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.implicitly_wait(50)
driver.maximize_window()

driver.get('https://www.flipkart.com/')
time.sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def handling_windows():
    return driver.window_handles

def switch_to_window(handle):
    return driver.switch_to.window(handle)

driver.find_element('xpath','//a[text()="Myntra"]').click()
time.sleep(3)
for handle in handling_windows():
    switch_to_window(handle)
    if 'myntra' in driver.current_url:
        driver.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('Sneakers')
        time.sleep(3)
        switch_to_window(handling_windows()[0])
        time.sleep(3)

driver.find_element('xpath', '//a[text()="Cleartrip"]').click()
time.sleep(3)
for handle in handling_windows():
    switch_to_window(handle)
    if 'cleartrip' in driver.current_url:
        driver.find_element('xpath', '//input[@id="mobile"]').send_keys('7204071688')
        time.sleep(3)
        switch_to_window(handling_windows()[0])
        time.sleep(3)

driver.find_element('xpath', '//a[text()="Shopsy"]').click()
time.sleep(3)
for handle in handling_windows():
    switch_to_window(handle)
    if 'shopsy' in driver.current_url:
        driver.find_element('xpath', '//div[text()="Login"]').click()
        time.sleep(3)
        switch_to_window(handling_windows()[0])
        time.sleep(3)
driver.quit()

















