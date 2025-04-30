from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path=r'D:\studybook\PC\python\PythonStudy\AJAX\chromedriver\chromedriver.exe'
server_pah=Service(driver_path)
driver=webdriver.Chrome(service=server_pah)
driver.get('http://exercise.kingname.info/exercise_advanced_ajax.html')
try:
    WebDriverWait(driver,30).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "content"), '通关'))
except Exception as _:
    print('网页加载太慢，不想等了。')

element = driver.find_elements(By.XPATH,'//div[@class="content"]')
element = driver.find_elements(By.ID,"passwd-id") 
element = driver.find_elements(By.NAME,"passwd")
for elements in element:
    print(f'异步加载的内容是：{elements.text}')

driver.quit()
# time.sleep(5)
# html=driver.page_source
# print(html)

# input('')