from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

url = 'https://www.uniqlo.com/tw/zh_TW/'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

women = driver.find_element(By.XPATH,'//*[@id="hmall-container"]/div/div[1]/div[2]/div/div/div/div/div[2]/span[1]')
# baby = driver.find_element(By.XPATH,'//*[@id="hmall-container"]/div/div[1]/div[2]/div/div/div/div/div[2]/span[4]/a')

action = ActionChains(driver)

action.move_to_element(women).perform()
time.sleep(2)

sale = driver.find_element(By.XPATH,'//*[@id="hmall-container"]/div/div[1]/div[3]/div[4]/div[2]/div/div/div[1]/div/div/div[21]/div/span')
# action.move_to_element(sale).click().perform()
sale.click()

WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.CLASS_NAME,'h-product-group'))
)

# products = driver.find_elements(By.CLASS_NAME,'product-li')
# print(products)

count = 0
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    products = driver.find_elements(By.CLASS_NAME,'product-li')
    # time.sleep(3)
    try:
        WebDriverWait(driver,5).until(
            EC.invisibility_of_element_located((By.CLASS_NAME,'loading-paging'))
            # EC.presence_of_element_located((By.CLASS_NAME,'loading-paging'))
        )
    except:
        pass
    if count == len(products):
        break
    count = len(products)


print(products)
print(len(products))

time.sleep(10)



driver.close()
