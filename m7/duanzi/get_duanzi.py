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

with open('duanzi.txt', 'w', encoding='utf-8') as f:
    for li in list_li:
        # ./div表示在当前循环的li标签下的div，继续查找
        content = li.xpath('./div[@class="content"]/text()')[0]
        title = li.xpath('./div[@class="info"]/a/text()')[0]

        f.write(title+'\n'+content+'\n\n')

print('段子抓取成功')

