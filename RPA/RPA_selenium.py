from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

PATH = r'C:\Python310\Lerning with loong\RPA\msedgedriver.exe'
service = Service(PATH)

driver = webdriver.Edge()
driver.get("https://uncle-tools.com/admin")

username = driver.find_element(By.NAME,'username')
username.send_keys('uncle')
time.sleep(3)

password = driver.find_element(By.NAME,'password')
password.send_keys('Admin12345')
time.sleep(3)
password.send_keys(Keys.RETURN)

url = 'https://uncle-tools.com/admin/myapp/product/add/'
driver.get(url)

name = driver.find_element(By.NAME,'name')
name.send_keys('mango')

price = driver.find_element(By.NAME,'price')
price.clear()
price.send_keys('25')

save = driver.find_element(By.NAME,'_save')
save.click()





time.sleep(60)
# driver.close()  # close browser but not close driver
driver.quit() #close driver suggest this method to protect os error