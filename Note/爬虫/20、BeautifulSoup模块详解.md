BeautifulSoup模块详解

在使用`bs4`模块前需要安装依赖模块`lxml`

`from bs4 import BeautifulSoup`



#### 创建BeautifulSoup对象的方法：

##### 1、打开本地图片：

`f = open('xxx')`

`BeautifulSoup(文件对象, 'lxml')`

##### 2、获取网络请求

`BeautifulSoup('网络请求数据', 'lxml')`



#### 调用`BeautifulSoup`对象的方法：

#### 1、查找到第一个符合要求的标签对象

##### `soup.p`：

`<p>把糗事百科加入收藏夹</p>`



##### `soup.a`：

`<a href="/"><h1>糗事百科</h1></a>`



#### 2、打印标签的属性值，结果字典类型

##### `soup.li.attrs`:

`{'id': 'vote-up-747512', 'class': ['up']}`

##### `soup.li['id']`:

`vote-up-2087026`



#### 3、获取标签的文本内容

#### 3.1、string属性

##### 如果标签下还有标签，那么string的结果为None

##### `soup.div.string`:

`None`



##### `soup.p.string`:

`把糗事百科加入收藏夹`



#### 3.2、text属性

##### `soup.p.text`:

`把糗事百科加入收藏夹`



##### `soup.div.text`

```
糗事百科
热门
24小时
热图
文字
穿越
糗图
新鲜
登录
```



#### 3.3、get_text()方法：

##### `soup.p.get_text()`:

`把糗事百科加入收藏夹`



#### 4、根据属性定位标签

##### `soup.find('a')`：

`<a href="/"><h1>糗事百科</h1></a>`



##### `soup.find('div', class_="logo")`:

```html
<div class="logo" id="hd_logo">
<a href="/"><h1>糗事百科</h1></a>
</div>
```



#### 5、获取所有的标签

查找到所有的指定标签，结果是一个列表

##### `ret = soup.findAll('a')`:

```
[<a href="/"><h1>糗事百科</h1></a>, <a href="/" rel="nofollow" target="_blank">热门</a>, <a href="/hot/" target="_blank">24小时</a>, <a href="/imgrank/" target="_blank">热图</a>...]
```



##### `soup.findAll('a', limit=2)`

`[<a href="/"><h1>糗事百科</h1></a>, <a href="/" rel="nofollow" target="_blank">热门</a>]`



##### 查找到所有的a标签和div标签

##### `soup.findAll(['a', 'div'])`：



#### 6、根据选择器查找到指定标签

标签选择器、类选择器，id选择器、层级选择器、后代选择器…，返回的结果永远是列表

得到结果是`bs4.Element.Tag`类型，可以继续使用`bs4`对象的方法

##### `soup.select(选择器)`



##### 6.1、根据id选择器查找标签

##### `soup.select('#login-form')`



##### 6.2、根据类选择器查找标签

##### `soup.select('.random')`



##### 6.3、根据后代选择器查找标签

##### `soup.select('.col1 .date')`



##### 6.4、根据属性选择查找标签

##### `soup.select('input[name="login"]')`



##### 6.5、层级选择器

##### `soup.select('#hd_logo > a')`