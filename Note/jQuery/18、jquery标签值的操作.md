值的操作

**Jquery：**text()       **js：**innerText()

**jquery：**html()      **js：**innerHtml()

**jquery：**val()         **js：**value()

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
    <div class="box">
        <p>滑翔机出场</p>
    </div>
    <p class="p">欢乐你我她</p>
    <input type="text" name="username" value="请填写用户名">
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        // 获取对象的标签内容，等价于JS对象的innerText()
        console.log($('.box').text());

        // 设置对象的标签内容
        console.log($('.box').text('暗黑破坏神'));

        // 输出<p>滑翔机出场</p>，等价于JS对象的innerHTML()
        console.log($('.box').html());
        
        // 将对象下的整个HTML结构替换掉
        $('.box').html('<h2>叫我写点什么</h2>');
        
        // 输出标签的的value属性
        console.log($('[name = username]').val());
        
        // 设置input标签的value值
        $('[name = username]').val('填啥用户名');

        // 清空value值
        $('[name = username]').val('');
    </script>
</body>
</html>
```

