import requests

session = requests.session()

login_url = 'http://my.iciba.com/index.php?c=sso&m=web_login'
site_url = 'http://my.iciba.com/?c=user'

params = {
    'username': 'music51555',
    'password': 'nishi458',
    'remember': '0',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

# session_response = session.post(url = login_url, params = params, headers = headers)

# response = session.get(url = site_url,headers = headers)

response = requests.get(url = site_url,headers = headers)

with open('self_site.html', 'w', encoding='utf-8') as f:
    f.write(response.text)