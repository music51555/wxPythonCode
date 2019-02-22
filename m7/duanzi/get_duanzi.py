import requests
from bs4 import BeautifulSoup

index_url = 'https://ishuo.cn/'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

index_text = requests.get(url = index_url, headers = headers).text

soup = BeautifulSoup(index_text,'lxml')

print(soup.select('a[href="/member/4"]'))
