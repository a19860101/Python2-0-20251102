from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'

driver.get(url)

driver.maximize_window()

# getNewRate = driver.find_element(By.XPATH,'//*[@id="ie11andabove"]/div/p[1]/a[1]')
getNewRate = driver.find_element(By.LINK_TEXT, '取得最新報價')

time.sleep(5)

getNewRate.click()

time.sleep(5)

driver.close()