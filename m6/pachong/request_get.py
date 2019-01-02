import requests

url = 'https://www.sogou.com/web?query=可口可乐&ie=utf8'

response = requests.get(url)

print(response.text)

with open('zhou.html', 'w', encoding='utf-8') as f:
    f.write(response.text)