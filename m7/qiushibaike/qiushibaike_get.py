import requests

url = 'https://www.qiushibaike.com/text/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

for i in range(10):
    params = {
        'page':i
    }

    response = requests.get(url = url, params = params, headers = headers)

    print(response.text)