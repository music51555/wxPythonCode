import requests

from lxml import etree
from yundama.get_code import *
import re

url = 'http://www.douban.com/accounts/login'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

login_response = requests.get(url =url, headers = headers)

tree = etree.HTML(login_response.text)

img_url = tree.xpath('//*[@id="captcha_image"]/@src')[0]
print(img_url)

valicode_img_response = requests.get(url = img_url, headers = headers)

with open('../yundama/valicode_img.png', 'wb') as f:
    f.write(valicode_img_response.content)

valicode_text = get_valid_code('../yundama/valicode_img.png').lower()

print(valicode_text)

valid_code_id = re.findall('id=(?P<key>.*)&size', img_url)

login_post_url = 'https://accounts.douban.com/login'

data = {
    'source': None,
    'redir': 'https://www.douban.com/',
    'form_email': '18611848257',
    'form_password': 'nishi458_2',
    'captcha-solution': valicode_text,
    'captcha-id': valid_code_id[0],
    'login': '登录',
}

index_text = requests.post(url = login_post_url, data = data, headers = headers).text

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_text)










