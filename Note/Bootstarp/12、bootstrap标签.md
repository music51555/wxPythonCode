bootstrap标签

`label`类，将span设置为标签样式

`label-default`、`label-primary`、`label-success`、`label-info`、`label-warning`、`label-danger`类，为标签设置颜色样式

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
            <div class="col-md-3">
                <div class="thumbnail">
                    <!-- label类，添加为标签样式 -->
                    <!-- label-info类，设置标签的颜色样式-->
                    <h3>Example heading <span class="label label-info">New</span></h3>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

