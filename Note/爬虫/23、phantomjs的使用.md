`phantomjs`的使用 ` fanˈtəm/` 幽灵，幻影

无界面的浏览器

**下载驱动：**`http://phantomjs.org/download.html`

**知识点1：**调用`driver`对象的`save_screenshot()`方法截图浏览器界面

**知识点2：**`webdriver.PhantomJS()`实例化浏览器驱动对象，方法名大写

```python
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
```

