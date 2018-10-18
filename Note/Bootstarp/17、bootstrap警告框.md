bootstrap警告框

`alert`类：使警告框增加padding、border等属性，形成一个面板样式的alert

`alert-success`类：改变alert面板颜色

`alert-link`类：使链接文字加粗

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
                <div class="thumbnail">
                    <!-- alert类使警告框增加padding、border等属性，形成一个面板样式的alert -->
                    <!-- alert-success改变alert面板颜色 -->
                    <div class="alert alert-success" role="alert">
                        这是警告框
                        <!-- 添加一个关闭按钮 -->
                        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="alert alert-info" role="alert">这是警告框
                        <!-- 添加一个a标签变为alert中的链接，alert-link类使链接文字加粗 -->
                        <a href="" class="alert-link">这是链接</a>
                    </div>
                    <div class="alert alert-warning" role="alert">这是警告框</div>
                    <div class="alert alert-danger" role="alert">这是警告框</div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

