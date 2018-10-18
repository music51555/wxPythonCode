bootstrap按钮

`role="button`属性：如果使用a作为按钮，a标签不是作为跳转链接的话，必须为其添加

`btn-lg`、`btn-sm`、`btn-xs`类，改变按钮尺寸大小

`btn-block`类：将按钮拉伸到100%的宽度，独占一行

`active`类：按钮的`active`类效果是，激活状态，实则是被点击下去

`disabled="disabled"`属性：按钮变为禁用状态

`btn-default`、`btn-primary`、`btn-info`、`btn-warning`、`btn-success`、`btn-danger`六种类，效果为改变按钮颜色样式

`img-rounded`、`img-circle`、`img-thumbnail`类，添加border后，图片分别被增加一些弧度、圆形、边框

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
        <div class="col-md-4">
            <!-- thumbnail  美 /'θʌmnel/   极小的 -->
            <div class="thumbnail">
                <form action="">
                    <div class="form-group">
                        <!-- 如果使用a作为按钮，a标签不是作为跳转链接的话，必须为其添加role="button" 属性-->
                        <!-- 同时为按钮添加btn-lg、btn-sm、btn-xs类，为其改变大小尺寸 -->
                        <a href="#" class="btn btn-default btn-lg" role="button">默认按钮</a>
                        <a href="#" class="btn btn-primary btn-sm" role="button">首选项</a>
                        <a href="#" class="btn btn-info btn-xs" role="button">一般信息</a>
                        <!-- 为按钮添加btn-block类，将其拉伸到100%的宽度 -->
                        <a href="#" class="btn btn-warning btn-block active" role="button">警告信息</a>
                        <!-- 为按钮添加active类，使其展示效果为被激活状态，效果实则是被点击下去 -->
                        <a href="#" class="btn btn-success active" role="button">成功</a>
                        <!-- 添加 disabled="disabled"属性，使按钮变为禁用状态-->
                        <a href="#" class="btn btn-danger" role="button" disabled="disabled">危险</a>
                        <a href="#" class="btn btn-link" role="button">链接</a>
                    </div>
                </form>
            </div>
        </div>
        <div class="col-md-4">
            <div class="thumbnail">
                <form action="">
                    <div class="form-group">
                         <!-- 按钮颜色样式-->
                        <button type="button" class="btn btn-default">（默认样式）Default</button>
                        <button type="button" class="btn btn-primary">（首选项）Primary</button>
                        <button type="button" class="btn btn-success">（成功）Success</button>
                        <button type="button" class="btn btn-info btn-block">（一般信息）Info</button>
                        <button type="button" class="btn btn-warning">（警告）Warning</button>
                        <button type="button" class="btn btn-danger">（危险）Danger</button>
                        <button type="button" class="btn btn-link">（链接）Link</button>
                    </div>
                </form>
            </div>
        </div>
        <div class="col-md-4">
            <!-- 在图片大小的基础上，使外边框的角度增加一些弧度 -->
            <img src="./images/101.png" class="img-rounded" alt="">

            <!-- 使图片包裹在圆形中 -->
            <img src="./images/101.png" class="img-circle" alt="">

            <!-- 使图片包裹在盒子边框中 -->
            <img src="./images/101.png" class="img-thumbnail" alt="">
        </div>
    </div>
</body>
</html>
```

