from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://google.com')

driver.maximize_window()

driver.save_screenshot('google.png')

driver.get('https://www.lccnet.com.tw/lccnet')

driver.save_screenshot('lccnet.png')


time.sleep(3)

driver.close()