from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import  ActionChains
from selenium.webdriver.common.by import By

url = 'https://www.uniqlo.com/tw/zh_TW/'

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)

driver.get(url)
driver.maximize_window()

action = ActionChains(driver)

account = driver.find_element(By.XPATH, '//*[@id="page-header"]/div/div/div/div[3]/ul/li[4]/a/i')

account.click()

time.sleep(5)

email = driver.find_element(By.XPATH, '//*[@id="hmall-container"]/div/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div/div[1]/input')
# email.click()
# email.send_keys('a19860101@gmail.com')

pw = driver.find_element(By.XPATH, '//*[@id="hmall-container"]/div/div[1]/div/div[2]/div/div/div[2]/form/div[2]/div/div/input[2]')
# pw.click()
# pw.send_keys('1a2s3d4f@')


btn = driver.find_element(By.XPATH,'//*[@id="hmall-container"]/div/div[1]/div/div[2]/div/div/div[2]/form/div[3]/div/button')
# btn.click()

action.click(email).send_keys('a19860101@gmail.com').pause(2).click(pw).send_keys('1a2s3d4f@').pause(2).click(btn).perform()

time.sleep(5)
driver.close()