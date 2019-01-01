import requests

url = 'https://www.douban.com/accounts/login'

data = {
    'source': 'index_nav',
    'form_email': '18611848257',
    'form_password': 'nishi458_2',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

response = requests.post(url = url, data = data, headers = headers)

with open('./douban.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
