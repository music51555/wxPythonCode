`requests`抓取多页关键词的搜索结果



指定搜索关键词，和起始搜索页数、结尾搜索页数，变为`range(1, 3)`来每次把`params`中的`page`参数进行变换，将每次请求的数据存储为一个文件

```python
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
```



抓取糗事百科数据：

```python
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
```

