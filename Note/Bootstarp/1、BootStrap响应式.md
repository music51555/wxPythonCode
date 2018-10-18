**响应式：**根据浏览器的窗口大小，页面内容会自动调整，如同时可以在电脑端和手机端浏览，所以开发一套代码，可以在任何设备上正常显示



@media screen and (min-width、max-width)

max-width：定义页面中最大的可视宽度

min-width：定义页面中最小的可视宽度

**准备工作：**

**1、meta标签**

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0 user-scalable=no">
```

**2、加载兼容文件，如兼容IE**

```html
[if lt IE 9]>
　　<script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
　　<script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
<![endif]
```

**3、IE-Edge**

```html
<meta http-equiv="X-UA-Compatible" content="ie=edge">
```

代码

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0 user-scalable=no">
    <!--[if lt IE 9]-->
　　<script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
　　<script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
<!--[endif]-->
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        /* 表示浏览器宽度最小达到1200px时body背景色呈红色 */
        @media screen and (min-width:1200px){
            body{
                background-color: red;
            }
        }
        /* 表示浏览器宽度最小达到960px，最大达到1199px时body背景色呈红色 */
        @media screen and (min-width:960px) and (max-width:1199px){
            body{
                background-color: yellow;
            }
        }
        /* 表示浏览器宽度最大达到959px时body背景色呈红色 */
        @media screen and (max-width:959px){
            body{
                background-color: green;
            }
        }
    </style>
</head>
<body>
    
</body>
</html>
```