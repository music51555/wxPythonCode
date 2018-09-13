从交互的角度，描述行为，提升用户体验

布兰登·艾奇

**ECMAScript**：定义了js的标准语法

**DOM**：Document Object Model，操作文档页面上元素的API

**BOM**：Browser Object Model，操作浏览器上的部分API



**引入js**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/javascript">

    </style>
</head> 
<body>
    <!-- 内接式，js语句以分号结尾 -->
    <script type="text/javascript">
        alert("alex");
    </script>

    <!-- 外接式引入js脚本，在src参数写路径，script标签可以写在任何地方 -->
    <script type="text/javascript" src="./js/index.js"></script>
</body>
</html>
```



**js语句**

```javascript
//注释方法	
//弹出警告框
alert("alex");

//在控制台Console中输出内容
console.log("alex");
```

