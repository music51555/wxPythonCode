import requests

url = 'http://www.baidu.com/s?'

params = {
    'ie': 'utf-8',
    'wd': 'ip',
}

proxy = {
    'http': '112.217.199.122:55872'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

response = requests.get(url = url, params=params, proxies = proxy, headers = headers)

with open('ip.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
