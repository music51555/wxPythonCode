xpath之抓取段子

**知识点1：**通过`xpath`获取到的元素类型为`Element`，该类型可以继续使用`xpath`解析数据

**知识点2：**循环通过`xpath`得到的列表元素，每一个元素的类型是`Element`，当调用`xpath`方法时，使用了`./div`时，表示当前循环对象下的`div`标签，继续查找

```python
import requests
from lxml import etree

index_url = 'https://ishuo.cn/'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

index_text = requests.get(url = index_url, headers = headers).text

etree = etree.HTML(index_text)

# 通过xpath得到的所有标签对象类型是<Element li at 0x1107c3448>，该对象可以继续进行xpath解析
list_li = etree.xpath('//li[@class="list_li"]')

# 打开一个文件，循环写入标题和内容
with open('duanzi.txt', 'w', encoding='utf-8') as f:
    for li in list_li:
        # ./div表示在当前循环的li标签下的div，继续查找
        content = li.xpath('./div[@class="content"]/text()')[0]
        title = li.xpath('./div[@class="info"]/a/text()')[0]

        f.write(title+'\n'+content+'\n\n')
        
print('段子抓取成功')
```

