bootstarp面板

data-xxx属性与JS有关

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
                    <!-- 通过修改panel-success，可以将面板的边框设置为不通的颜色 -->
                    <div class="panel panel-success">
                        <!-- panel-body类，为盒子添加padding:15px，形成面板效果 -->
                        <div class="panel-body">
                            Basic panel example
                        </div>
                    </div>                   
                </div>
            </div>
            <div class="col-md-4">
                <!-- 带标题栏的面板，实则就是2个面板， -->
                <!-- 在最外层的面板上，增加panel-primary等属性，可以将面板的标题栏颜色和边框颜色 -->
                <div class="panel panel-default panel-primary">
                    <!-- 只不过panel-heading类为面板增加了标题背景色等属性 -->
                    <div class="panel-heading ">Panel heading without title</div>
                    <div class="panel-body">
                        Panel content
                    </div>
                </div>

                <div class="panel panel-default">
                    <div class="panel-heading">
                        <h3 class="panel-title">Panel title</h3>
                    </div>
                    <div class="panel-body">
                        Panel content
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
<script type="text/javascript" src="./js/jquery.min.js"></script>
<script type="text/javascript" src="./bootstrap-3.3.7/js/bootstrap.min.js"></script>
</html>
```

