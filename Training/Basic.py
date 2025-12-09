import time

''' Initializing Chrome Browser '''
#from selenium import webdriver
#c_driver = webdriver.Chrome()      ## obj_name = ClassName()
#time.sleep(20)

#The Above Command Will Close The Browser Automatically
#To Prevent The Browser From Automatically Closing

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
c_driver = webdriver.Chrome(opts)

''' Initializing Firefox Browser '''
#from selenium import webdriver
#f_driver = webdriver.Firefox()     ## obj_name = ClassName()

#Firefox Will Not Close Automatically
#So No Need To Consider FirefoxOptions and add_experimental_option

''' Initializing Edge Browser '''
#from selenium import webdriver
#e_driver = webdriver.Edge()         ## obj_name = ClassName()

from selenium import webdriver
opts = webdriver.EdgeOptions()
opts.add_experimental_option("detach", True)
c_driver = webdriver.Edge(opts)