from bs4 import BeautifulSoup
import requests

url = 'https://www.qiushibaike.com/history/'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

index_text = requests.get(url = url, headers = headers).text

# 打印soup对象，得到的是整张html网页的内容，标签+文本内容
soup = BeautifulSoup(index_text, 'lxml')

ret = soup.select('#hd_logo > a')
print(ret)