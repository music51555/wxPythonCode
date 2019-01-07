import requests
from bs4 import BeautifulSoup

shuihu_url = 'http://www.shicimingju.com/book/shuihuzhuan.html'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

shuihu_index = requests.get(url = shuihu_url, headers = headers).text

soup = BeautifulSoup(shuihu_index, 'lxml')

def get_content(full_content_url):
    content_index = requests.get(url=full_content_url, headers=headers).text
    content_soup = BeautifulSoup(content_index, 'lxml')
    # 如果使用select获取文章详情页正文的class标签，那么得到的是结果永远是列表，存储的当前标签对象，包含所有子标签
    # content = content_soup.select('.chapter_content')[0].text
    # 使用find得到的直接是当前标签对象，并包含所有子标签
    content = content_soup.find('div', class_='chapter_content').text
    return content

title_list = soup.select('.book-mulu a')

with open('shuihu.txt', 'w', encoding='utf-8') as f:
    for title_tag in title_list:
        content_url = title_tag['href']
        full_content_url = 'http://www.shicimingju.com'+content_url
        content = get_content(full_content_url)
        f.write(title_tag.text+'\n'+content+'\n\n')

