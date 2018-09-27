jquery属性操作

**html属性操作**

**js中**
**获取属性值：**getAttribute
**设置属性值：**setAttribute

**jquery中**
**获取属性值：**jqueryobj.**attr(属性)**
**设置属性值：**jqueryobj.**attr(属性，属性值)**

jqueryobj.attr{
    属性1：属性值1，
    属性2：属性值2
}

**删除属性值**：
**removeAttr(属性)**
但是不建议设置class属性，因为原来的类会被替换掉，建议使用类样式属性操作：addClass和removeClass

```html


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        .box{
            width: 100px;
            height: 100px;
            background-color:red;
        }
    </style>
</head>
<body>
    <a href="" id="baidu">baidu</a>
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        $(function(){
            // 可以设置单个属性，也可以设置多个属性
            $('a').attr({
                'name':'baidu',
                'href':'https://www.baidu.com/'
            });
            $('a').removeAttr('id');
        })
    </script>
</body>
</html>
```



**样式属性操作**

```javascript
jqueryobj.css('样式名称','样式内容');
jqueryobj.css{
    '样式一'：'样式内容一'，
    '样式二'：'样式内容二'
};
```