bootstarp进度条

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
                    <!-- 普通样式的进度条，更改 style="width: 60%;"改变进度条长度-->
                    <div class="progress">
                        <div class="progress-bar " role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%;">
                            60%
                        </div>
                    </div>      
                    <!-- 在展示很低的百分比时，如果需要让文本提示能够清晰可见，可以为进度条设置 min-width 属性 -->
                    <div class="progress">
                        <div class="progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="min-width: 2em;">
                            20%
                        </div>
                    </div>      
                    <div class="progress">
                        <!-- 添加progress-bar-success类，使进度条的颜色改变 -->
                        <!-- 添加progress-bar-striped类，是进度条变为条纹状 -->
                        <!-- 添加active类，使进度条变为动画效果 -->
                        <div class="progress-bar progress-bar-success progress-bar-striped active" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 80%;">
                            80%
                        </div>
                    </div>         
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

