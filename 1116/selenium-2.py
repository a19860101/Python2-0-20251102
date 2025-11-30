from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://google.com')
driver.maximize_window()
time.sleep(1)

search = driver.find_element(By.CLASS_NAME,'gLFyf')
time.sleep(1)

search.send_keys('h')
time.sleep(1)
search.send_keys('e')
time.sleep(3)
search.send_keys('l')
time.sleep(2)
search.send_keys('l')
time.sleep(4)
search.send_keys('o')
time.sleep(1.5)

search.send_keys(Keys.ENTER)

time.sleep(3)

driver.close()
