！important

在标签选择器中添加！important，使选择器的权重最高，优先使用

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>!important</title>

    <style type="text/css">
        /* 第1个标签选择器的权重大于第二个标签选择器，但在第2个标签选择器中添加了！important，使它的权重最高，优先使用 */
        #box1 #box2 .wrap3{
            color: red;
            font-size: 50px;
        }

        #box2 .wrap3{
            color: blue !important;
            font-size: 30px;
        }
    </style>
</head>
<body>
    <div class="wrap1" id="box1">
        <div class="wrap2" id="box2">
            <div class="wrap3" id="box3">
                <p>这是一个段落</p>
            </div>
        </div>
    </div>
</body>
</html>
```



当标签选择器都是继承而来的时，此时比较标签描述，哪个更近则使用哪个，如果此时添加

！important关键字是不影响选择效果的

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>!important</title>

    <style type="text/css">
        /* 选择器1和选择器2都是继承而来的样式，权重都为0，此时判断看谁描述的更近、更精确，蓝色字体样式描述的更精确，但红色字体样式添加了！important，不影响判断描述精确度的这种情况 */
        #box1 .wrap2{
            color: red !important;
            font-size: 50px;
        }

        .wrap1 #box2 .wrap3{
            color: blue;
            font-size: 30px;
        }
    </style>
</head>
<body>
    <div class="wrap1" id="box1">
        <div class="wrap2" id="box2">
            <div class="wrap3" id="box3">
                <p>这是一个段落</p>
            </div>
        </div>
    </div>
</body>
</html>
```



在继承的标签选择器中添加！important，权重仍然小于选中的标签选择器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>!important</title>

    <style type="text/css">
        /* ！important应用于权重比例不等时的标签选择器，在权重比例低的选择器中添加，则使当前选择器的权重最高 */
        #box1 #box2{
            color: red !important ;
            font-size: 50px;
        }

        #box1 #box2 .wrap3 p{
            color: blue  ;
            font-size: 30px ;
        }
    </style>
</head>
<body>
    <div class="wrap1" id="box1">
        <div class="wrap2" id="box2">
            <div class="wrap3" id="box3">
                <p>这是一个段落</p>
            </div>
        </div>
    </div>
</body>
</html>
```

