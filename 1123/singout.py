from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

url = 'https://member.lccnet.com.tw/signout/LearningRecord.aspx'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

phone = '0912345678'

target = driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div/form/div/div[2]/div/div[1]/div[2]/div[2]/input')
target.send_keys(phone)
target.send_keys(Keys.ENTER)



time.sleep(10)

driver.close()

