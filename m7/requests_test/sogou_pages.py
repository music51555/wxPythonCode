import requests

key_word = input('请输入搜索的关键词：')

start_page = int(input('请输入查询结果的起始页数'))

end_page = int(input('请输入查询结果的结尾页数'))

url = 'https://www.sogou.com/web?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

for page in range(start_page, end_page):

    params = {
        'query': key_word,
        'page': page,
        'ie': 'urf8'
    }

    response = requests.get(url = url, params = params, headers = headers)

    with open(
            '搜狗%s关键词第%s页的数据'%(key_word, page)+'.html','w', encoding='utf-8') as f:
        f.write(response.text)