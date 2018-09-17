标签对象的client参数

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
            width: 200px;
            height: 200px;
            border: 10px solid red;
            padding: 80px;
        }
    </style>
</head>
<body>
    <div id="box">
        这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容
    </div>、
    <script type="text/javascript">
        var divobj = document.getElementById('box');
        // client.top表示内容区域到边框的顶部，实则就是顶端边框的宽度
        console.log(divobj.clientTop);
        // client-left表示内容区域到左边框的外边距，实则就是左边框的宽度
        console.log(divobj.clientLeft);
        // client.width和client-height表示内容区域+padding的高度、宽度，实则就是内容显示区域的距离
        console.log(divobj.clientWidth);
        console.log(divobj.clientHeight);
    </script>
</body>
</html>
```

