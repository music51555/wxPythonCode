bootstrap辅助类

`text-muted`、柔和的  美 /mjut/，`text-primary`、`text-info`、`text-warning`、`text-success`、`text-danger`类，为改变文字颜色样式

`close`类，关闭按钮类，将按钮放置在盒子右上角

`&times;`是根据HTML特殊字符编码对照表显示为x

`caret`类，放置在`span`标签中，将其变为一个倒三角样式，如果在父盒子添加`dropup`类，那么倒三角将变为正三角样式

`pull-left`类，将盒子设置为左浮动

`pull-right`类，将盒子设置为右浮动

`clearfix`类，在盒子层级清除浮动

`center-block`类，将盒子居中显示

`show`类，显示盒子元素

`hiddent`类，隐藏盒子元素

&times;是根据HTML特殊字符编码对照表显示为

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
                    <p class="bg-primary">id dolor id nibh ultricies vehicula ut id elit.</p>
                    <p class="bg-info">id dolor id nibh ultricies vehicula ut id elit.</p>
                    <p class="bg-warning">id dolor id nibh ultricies vehicula ut id elit.</p>
                    <p class="bg-success">id dolor id nibh ultricies vehicula ut id elit.</p>
                    <p class="bg-danger">id dolor id nibh ultricies vehicula ut id elit.</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="thumbnail">
                    <!-- muted  柔和的  美 /mjut/ -->
                    <!-- 添加text-hide等类为文本添加颜色，使盒子中的内容隐藏 -->
                    <p class="text-muted text-hide">id nibh ultricies vehicula ut id elit.</p>
                    <p class="text-primary">id nibh ultricies vehicula ut id elit.</p>
                    <p class="text-info">id nibh ultricies vehicula ut id elit.</p>
                    <p class="text-warning">id nibh ultricies vehicula ut id elit.</p>
                    <p class="text-success">id nibh ultricies vehicula ut id elit.</p>
                    <p class="text-danger">id nibh ultricies vehicula ut id elit.</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="thumbnail" style="height: 336px">
                    <!-- 关闭图标 。close类使其在盒子的右上角显示，&times;是根据HTML特殊字符编码对照表显示为X-->
                    <button type="button" class="close" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                    <!-- span标签中的caret类，使其变为一个向下的三角-->
                    <!-- 如果在父盒子添加dropup类，则向下的三角变为向上 -->
                    <div class="dropup">
                        <span class="caret"></span>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <!-- 在父盒子添加clearfix类，可以使盒子清除浮动 -->
            <div class="col-md-4 clearfix">
                <!-- pull-left和pull-right可以是盒子左浮动和右浮动 -->
                <div class="pull-left" style="border: 1px solid red;width: 100px;height: 100px"></div>
                <!-- 为盒子添加center-block类，使盒子居中显示 -->
                <div class="center-block" style="border: 1px solid red;width: 100px;height: 100px"></div>
                <!-- 为盒子添加show、hidden类，使盒子隐藏显示 -->
                <div class="pull-right hidden" style="border: 1px solid red;width: 100px;height: 100px"></div>
            </div>
        </div>
    </div>
</body>
</html>
```

