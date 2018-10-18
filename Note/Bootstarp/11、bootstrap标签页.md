bootstarp标签页

`nav`类：所有导航组件，都依赖于nav类

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="./bootstrap-3.3.7/css/bootstrap.css">
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-md-4">
                <!-- bootstarp中的所有导航组件，都依赖于nav类 -->
                <ul class="nav nav-tabs">
                    <li role="presentation" class="active">
                        <a href="">首页</a>
                    </li>
                    <li role="presentation">
                        <a href="">资讯</a>
                    </li>
                    <li role="presentation">
                        <a href="">团购</a>
                    </li>
                </ul>
            </div>
            <div class="col-md-4">
                <!-- 为标签添加了蓝色背景色 -->
                <ul class="nav nav-pills">
                    <li role="presentation" class="active">
                        <a href="">首页</a>
                    </li>
                    <li role="presentation">
                        <a href="">资讯</a>
                    </li>
                    <li role="presentation">
                        <a href="">团购</a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</body>
<script type="text/javascript" src="./js/jquery.min.js"></script>
<script type="text/javascript" src="./bootstrap-3.3.7/js/bootstrap.min.js"></script>
</html>
```

