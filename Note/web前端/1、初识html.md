HTML编写的是静态网页：没有与用户交互，只有读者进行浏览

**结构：**HTML

**表现：**CSS

**行为：**JavaScript

HTML：Hyper Text Markup Language 超文本标记语言 美  ['haɪpɚ] 亢奋的

CSS：层叠样式表

JavaScript：网页的脚本语言

后缀名：.html

**固定结构**

```html
<!DOCTYPE HTML><!--文档声明类型，必须写在文档的第一行-->
<html>    <!--根标签-->
    <head>...</head><!--头部元素容器，一般放入<title>、<script>、<style>、<link>、<meta>-->
    <body>...</body><!--网页的主要内容-->
</html>
```



```html
<!DOCTYPE html> <!--声明文档的类型，标记文档为html5的文件-->
<html>
    <head>
        <meta charset="utf-8"/>
        <!--包含头部信息-->
    </head>
    <body>
        <!--包含浏览器显示的内容-->
        这是我们的文档结构
    </body>
</html>
```



在浏览器输入网址后，浏览器做了什么？

1、用户输入网址

2、浏览器首先会检查浏览器的缓存中是否有这个域名的IP地址解析结果

3、再检查操作系统的缓存文件中是否有域名的解析结果

4、如果都没有，则会把域名发送给DNS服务器进行解析，解析完成后将结果返回给浏览器，DNS服务器部署在网络供应商

5、浏览器IP地址与目标web服务器在80端口上建立TCP连接

6、浏览器获取请求页面的html代码

7、浏览器渲染HTML页面

8、窗口关闭时，浏览器终止与服务器的连接





