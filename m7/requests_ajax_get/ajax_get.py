import requests

url = 'https://movie.douban.com/j/chart/top_list?'

params = {
    'type': '13',
    'interval_id': '100:90',
    'action': '',
    'start': '20',
    'limit': '50',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

response = requests.get(url = url, params = params, headers = headers)

print(response.text)
