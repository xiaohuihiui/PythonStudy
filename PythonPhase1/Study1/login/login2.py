from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver') 
driver.get("https://www.zhihu.com/#signin")

elem = driver.find_element_by_name("account") 
elem.clear()
elem.send_keys("xxx@gmail.com") 
password = driver.find_element_by_name('password') 
password.clear()
password.send_keys("12345678") 
input('')
elem.send_keys(Keys.RETURN) 
time.sleep(10) 
print(driver.page_source)
driver.quit()
