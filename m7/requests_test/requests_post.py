import requests

url = 'http://my.iciba.com/index.php?c=sso&m=web_login'

data = {
    'username': 'music51555',
    'password': 'nishi458',
    'remember': '0',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

response = requests.post(url = url, data = data, headers = headers)

print(response.text)
