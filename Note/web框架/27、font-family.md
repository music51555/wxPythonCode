**font-family**

使用英语的逗号隔开字体，以作备选之用，备选字体可以有无数个，将英文字体写在最前面

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=div, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        div{
            width: 300px;
            height: 175px;
            padding-top: 25px;
            border: 1px solid red;
            line-height: 30px;
            font-size: 16px;
            /* 使用英语的逗号隔开字体，以作备选之用，备选字体可以有无数个，将英文字体写在最前面 */
            font-family:"Times New Roman","微软雅黑","黑体","宋体";
        }
    </style>
</head>
<body>
    <div>
        这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容这是一些内容
    </div>
</body>
</html>
```

