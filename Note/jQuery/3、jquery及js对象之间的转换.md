jquery及js对象之间的转换

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
    <div class="box1"></div>
    <div id="box2"></div>
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        // $(function(){   jquery入口函数
        $(document).ready(function(){

            // 传入类选择器，打印jquery对象
            console.log($('.box1'));

            // 传入id选择器，打印jquery对象
            console.log($('#box2'));

            // 将jquery对象-->js对象，根据jquery对象的伪数组，打印js对象，在jquery都是API，除了length和索引
            console.log($('.box1')[0]);

            console.log($('#box2').get(0));

            // 打印js对象
            var box = document.getElementById('box2');
            console.log(box);

            // 将js对象-->jquery对象，直接将js对象放入$( )中，打印jQuery.fn.init [div#box2]
            console.log($(box));
    });
    </script>
</body>
</html>
```

