`scrapy`的代理操作

流程：在爬虫程序将`start_urls`交给引擎后，引擎在调度器中排列准备下载页面，在准备调用下载器时，在调度器和下载器之间会有一层下载中间件，拦截请求，并做更换`IP`的操作



1、在`middlewares.py`中，编辑`process_request()`方法，配置`request.meta['proxy']`为代理`IP`

```python
class ScrapyProDownloaderMiddleware(object):

    def process_request(self, request, spider):
        request.meta['proxy'] = 'https://182.88.26.203:9797'
```



2、在`settings.py`中开启`DOWNLOADER_MIDDLEWARES`设置

```python
DOWNLOADER_MIDDLEWARES = {
   'scrapy_pro.middlewares.ScrapyProDownloaderMiddleware': 543,
}
```

