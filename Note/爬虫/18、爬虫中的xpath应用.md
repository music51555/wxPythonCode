爬虫中的xpath应用：

#### 1、下载安装lxml



#### 2、引用from lxml import etree



#### 3、创建对象

**调用本地文件：**`tree = etree.parse('./test.html')`

**调用网络请求内容：**`etree.HTML(content_text)`



#### 4、调用对象方法

##### 4.1、按属性定位

`//div[@class = 'song']`



##### 4.2、层级索引定位，[2]表示查找到第2个索引位置的li标签

`//*[@id='index_header' and @class='index-head']`



##### 4.3、逻辑运算符定位

`//a[@href = '' and @class = 'du']`



##### 4.4、模糊匹配

**模糊匹配class属性中包含ng的标签**

`//*[contains(@class,'head')]`



**模糊匹配class属性以ta开头的标签**

`//*[starts-with(@id,'sug')]`



##### 4.5、获取文本

**获取某个标签的文本**

`//div[@class='content']/span/text()`



**获取标签下所有子标签的文本**

`//div[@class='song']//text()`



##### 4.6、获取属性值

`//div[@class='song']//li[2]/a/@href`