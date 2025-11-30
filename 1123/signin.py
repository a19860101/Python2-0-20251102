from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

url = 'http://attend.lccnet.com.tw/TeamRecord.aspx'

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()


sid = '106204764'

sid_ta = driver.find_element(By.XPATH,'//*[@id="sid"]')
sid_ta.send_keys(sid)
sid_ta.send_keys(Keys.ENTER)



time.sleep(10)

driver.close()
