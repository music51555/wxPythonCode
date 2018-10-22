**DOM对象的属性操作**

首先打印对象，查看对象的所有属性

**prop(属性值)**，获取对象的属性值

**prop(属性，属性值)**，设置对象的属性值

**removeProp(属性)**，删除对象的属性值

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
    <input type="radio" name="sex" checked>男
    <input type="radio" name="sex">女
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        // 首先打印对象，查看对象的所有属性，在__proto__下查看到很多对象的内置属性
        console.log($('input[type = radio]').eq(0));

        // 查看对象其中的checked属性，返回true，因为它的单选按钮被选中
        console.log($('input[type = radio]').eq(0).prop('checked'));
        
        // 设置对象的属性值，格式prop(属性，属性值)
        $('input[type = radio]').eq(0).prop('checked',false);
        
        // 删除对象的属性值
        $('input[type = radio]').eq(0).removeProp('accept');
    </script>
</body>
</html>
```

