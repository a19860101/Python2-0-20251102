from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
url = 'https://www.nike.com/tw/w/winter-essentials-e7sr'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

time.sleep(10)
try:
    modal_close = driver.find_element(By.XPATH,'//*[@id="modal-root"]/div/div/div/div/div/section/div/div[1]/button')
    modal_close.click()
    time.sleep(5)
except:
    pass

# driver.execute_script('window.scrollTo(0,1000)')
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight-1500)')
# time.sleep(5)
# product-card
count = 0
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight-1500)')
    try:
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element((By.CLASS_NAME,'loader-bar'))
        )
    except Exception as e:
        print(e)
    products = driver.find_elements(By.CLASS_NAME, 'product-card')
    if count == len(products):
        break
    count = len(products)

for product in products:
    titles = product.find_element(By.CLASS_NAME,'product-card__titles').text
    print(titles)

driver.close()
