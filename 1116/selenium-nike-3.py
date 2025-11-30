from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.nike.com/tw/w/mens-shoes-nik1zy7ok')
driver.maximize_window()

time.sleep(10)

modal_close = driver.find_element(By.XPATH,'//*[@id="modal-root"]/div/div/div/div/div/section/div/div[1]/button')
modal_close.click()
time.sleep(5)

# driver.execute_script('window.scrollTo(0,1000)')
driver.execute_script('window.scrollTo(0,document.body.scrollHeight-1500)')
time.sleep(5)
driver.close()
