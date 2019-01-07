from selenium import webdriver
import time

baidu = 'https://www.baidu.com/'

driver = webdriver.Chrome('../chromedriver_win32/chromedriver.exe')

driver.get(baidu)
time.sleep(3)

kw = driver.find_element_by_id('kw')
su = driver.find_element_by_id('su')

kw.send_keys('保温杯')
time.sleep(1)

su.click()

driver.quit()