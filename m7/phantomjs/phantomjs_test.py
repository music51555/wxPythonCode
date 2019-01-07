from selenium import webdriver
import time

driver = webdriver.PhantomJS('/Users/mac/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')

driver.get('https://www.baidu.com/')

time.sleep(3)

driver.save_screenshot('index.png')

kw = driver.find_element_by_id('kw')
kw.send_keys('你的名字')

time.sleep(3)

su = driver.find_element_by_id('su')
su.click()

driver.save_screenshot('result.png')

time.sleep(3)
driver.quit()