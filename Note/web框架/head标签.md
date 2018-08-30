head标签：

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <!--文档的属性信息，包含文档的标题、编码方式-->
        <meta charset="UTF-8">
        <!--文档的标题-->
        <title>百度一下</title>

        <!--指定文档的内容类型和编码类型，这一句必须写-->
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <!--5秒后重定向到指定网址，打开网页后5秒后跳转到指定网址-->
        <meta http-equiv="refresh" content="5,URL=https://www.luffycity.com">
        <!--让IE浏览器以最高级的模式渲染当前网页， 美 /kəm'pætəbl/兼容的；能共处的-->
        <meta http-equiv="x-ua-compatible" content="IE=edge">

        <!--优化搜索引擎，工作的时候必须写，在搜索引擎中搜索的关键字-->
        <meta name="keywords" content="meta总结,html meta,meta属性,meta跳转">
        <meta name="description" content="路飞学成">

        <!--定义文档与外部资源的关系，最常用的就是链接外部样式表，可以在检查中的Sources和Network标签中查看到引入的index.css文件，rel时relationship关系的意思，stylesheet是样式表的意思-->
        <link rel="stylesheet" type="text/css" href="index.css" />

        <!--定义内部样式表-->
        <style type="text/css">

        </style>

        <!--定义内容脚本文件-->
        <script type="text/javascript">

        </script>

        <script src=""></script>
    </head>
    <body>
		广东爱情故事
    </body>
</html>
```

