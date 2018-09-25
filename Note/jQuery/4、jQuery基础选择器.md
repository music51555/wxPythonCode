jQuery基础选择器

**标签选择器：**$('div')

**类选择器：**$('.box1')

**id选择器：**$('#box3')

**通配符选择器：**$('*')

**并集选择器：**$('.box1,div')

jquery事件的函数中this表示js对象，$(this)表示将js对象转换为jquery对象，调用jquery方法

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        div{
            width: 100px;
            height: 100px;
            background-color: red;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="box1">box1</div>
    <div class="box2">box2</div>
    <div id="box3">box3</div>
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        $(function(){
            // 标签选择器，jquery中的点击事件是click，js中是onClick
            $('div').click(function(){
                // jquery函数中的this，表示当前jquery伪数组对象中的js对象
                console.log(this);

                // 通过js对象打印innerText
                console.log(this.innerText);

                // 把js对象转换为jquery对象后，调用text()API打印标签内容
                console.log($(this).text());
            });

            // 类选择器
            $('.box1').click(function(){
                // jquery中的隐藏方法
                $(this).hide();
            });
            
            // id选择器
            $('#box3').click(function(){
                $(this).text();
            });
        })
    </script>
</body>
</html>
```

