jQuery的入口函数

对比于js的入口函数

1、覆盖现象

2、等待图片资源加载完成之后，才会调用

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        // 返回html文档的jquery对象
        console.log($(document));
        
        // 返回的是jquery对象的伪数组，所以添加索引后，打印JS对象，实现jquery对象到js对象的转换
        console.log($(document)[0]);

        // 1、入口函数，等待文档资源加载完毕后，调用入口函数方法
        $(document).ready(function(){
            alert(1);
        });

        // 2、简便的、常用的入口函数写法，不会覆盖前一个入口函数
        $(function(){
            alert(2);
        });

        // 如果想要使用js的window.onload方法，等待图片加载完成之后，则可以获取window的jquery对象
        $(window).ready(function(){
            console.log(3);
        })
        
        // 也不会被覆盖
        $(window).ready(function(){
            console.log(4);
        })
    </script>
</body>
</html>
```
