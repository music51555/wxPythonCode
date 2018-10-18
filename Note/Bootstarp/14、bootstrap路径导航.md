bootstrap路径导航

`breadcrumb`类，美 /krʌm/ 面包屑  弄碎 。在有序列表的ol外层添加breadcrumb类，使列表变成路径导航

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
                <div class="thumnail">
                    <!-- 添加breadcrumb类，呈现Home Library images路径导航 -->
                    <ol class="breadcrumb">
                        <li>
                            <a href="">Home</a>
                        </li>
                        <li>
                            <a href="">Library</a>
                        </li>
                        <li>
                            <a href="">images</a>
                        </li>
                    </ol>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

