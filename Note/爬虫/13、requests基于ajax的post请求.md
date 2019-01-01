`requests`基于`ajax`的`post`请求



查询肯德基餐厅的`ajax`的`post`请求，方式和`requests.post`是一样的

```python
import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

params = {
    'cname': '',
    'pid': '',
    'keyword': '北京',
    'pageIndex': '1',
    'pageSize': '10',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

response = requests.post(url = url, params = params,headers = headers)

print(response.text)
```



获取到的数据

```json
{"Table":[{"rowcount":69}],"Table1":[{"rownum":1,"storeName":"育慧里","addressDetail":"小营东路3号北京凯基伦购物中心一层西侧","pro":"Wi-Fi,店内参观,礼品卡","provinceName":"北京市","cityName":"北京市"},{"rownum":2,"storeName":"京通新城","addressDetail":"朝阳路杨闸环岛西北京通苑30号楼一层南侧","pro":"Wi-Fi,点唱机,店内参观,礼品卡,生日餐会","provinceName":"北京市","cityName":"北京市"},{"rownum":3,"storeName":"黄寺大街","addressDetail":"黄寺大街15号北京城乡黄寺商厦","pro":"Wi-Fi,店内参观,礼品卡,生日餐会","provinceName":"北京市","cityName":"北京市"},{"rownum":4,"storeName":"四季青桥","addressDetail":"西四环北路117号北京欧尚超市F1、B1","pro":"Wi-Fi,店内参观,礼品卡,生日餐会","provinceName":"北京市","cityName":"北京市"},{"rownum":5,"storeName":"亦庄","addressDetail":"北京经济开发区西环北路18号F1＋F2","pro":"Wi-Fi,店内参观,礼品卡,生日餐会","provinceName":"北京市","cityName":"北京市"},{"rownum":6,"storeName":"石园南大街","addressDetail":"通顺路石园西区南侧北京顺义西单商场石园分店一层、二层部分","pro":"Wi-Fi,店内参观,礼品卡","provinceName":"北京市","cityName":"北京市"},{"rownum":7,"storeName":"北京站广场","addressDetail":"北京站一层","pro":"礼品卡","provinceName":"北京市","cityName":"北京市"},{"rownum":8,"storeName":"北京南站","addressDetail":"北京南站候车大厅B岛201号","pro":"礼品卡","provinceName":"北京市","cityName":"北京市"},{"rownum":9,"storeName":"北清路","addressDetail":"北京北清路1号146区","pro":"Wi-Fi,店内参观,礼品卡","provinceName":"北京市","cityName":"北京市"},{"rownum":10,"storeName":"大红门新世纪肯德基餐厅","addressDetail":"海户屯北京新世纪服装商贸城一层南侧","pro":"Wi-Fi,店内参观,礼品卡","provinceName":"北京市","cityName":"北京市"}]}
```

