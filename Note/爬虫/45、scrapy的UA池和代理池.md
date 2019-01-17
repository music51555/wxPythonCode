scrapy的UA池和代理池



定义`UA`池和代理池列表



**知识点1：**在项目的`middleware.py`中编写中间件类，编写其中的`process_request`方法

**知识点2：**`UA`池的中间件类需要继承于`UserAgentMiddleware`，从
`from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware`

**知识点3：**如何在列表中随机选择一个值，通过`random.choice(list)`

```python
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

user_agents = [
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
		'Opera/8.0 (Windows NT 5.1; U; en)',
		'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
		'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
		'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
		'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
		'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
		'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
		'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
		'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
		'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ',
	]

proxy_http = [
    '185.37.213.76:30695',
    '180.180.218.204:51565',
    '109.87.45.248:52566',
]

proxy_https = [
    '177.234.19.50:3128',
    '181.129.147.26:32945',
    '109.236.81.59:1080',
]

class MyUserAgentMiddleware(UserAgentMiddleware):

    def process_request(self, request, spider):
        ua = random.choice(user_agents)
        request.headers.setdefault('User-Agent',ua)


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        if 'https' in request.url:
            proxy_ip = random.choice(proxy_http)
            request.meta['proxy'] = 'https://'+proxy_ip
        else:
            proxy_ip = random.choice(proxy_https)
            request.meta['proxy'] = 'http://'+proxy_ip
```



最后再`settings.py`中开启中间件

```python
DOWNLOADER_MIDDLEWARES = {
   'wangyiPro.middlewares.WangyiproDownloaderMiddleware': 543,
   'wangyiPro.middlewares.MyUserAgentMiddleware': 542,
   'wangyiPro.middlewares.ProxyMiddleware': 541,
}
```

