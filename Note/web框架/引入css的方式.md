层叠样式表 **C**ascading **S**tyle **S**heets 

美化HTML页面

1. 将HTML页面的内容与样式分离。
2. 提高web开发的工作效率。

通过link标签引入css样式表，在rel参数用将css和html文件建立关系

也可以在其他css文件中，引入其他css文件

引入css的三种方式：

**1、内嵌方式，标签选择器**

```html
<style type="text/css">
	<!--作用于文档内的指定标签，如span标签-->
	span{
        color: red
	}
</style>
```



**2、行内样式**

```html
<!--在标签的一行之内写上CSS样式-->
<p style="color: blue;">这是一个段落</p>
```



**3、外接样式**

**3.1、通过link标签外链，推荐使用link**

```html
<!--relation表示关系，和外界的css建立关系-->
<link rel="stylesheet" href="./css/index.css">
```

**3.1、通过import导入**

```html
<!--在import结束后，要添加分号-->
<style type="text/css">
	@import url("./css/index.css");
<style>
```

也可以在外接的css文件中，引入其他css文件，如index.css，但import语句必须写在文件开头

```css
/* a{
    font-size: 30px;
} */
@import url("./content.css")
```

