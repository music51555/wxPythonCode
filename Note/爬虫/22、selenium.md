`selenium`之爬取动态加载的数据

`selenium`：让浏览器完成自动化的操作

**安装：**`pip3 install selenium`

**驱动：**`http://chromedriver.storage.googleapis.com/index.html`

**映射：**`https://www.cnblogs.com/JHblogs/p/7699951.html`



**知识点1：**创建`driver`对象`webdriver.Chrome('../chromedriver_win32/chromedriver.exe')`

**知识点2：`driver`**对象有各种查找标签的方法，支持`send_keys、click`等

```python
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
```
