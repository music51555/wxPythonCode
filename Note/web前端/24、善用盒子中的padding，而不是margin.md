**善用盒子中的padding，而不是margin**

![善用padding](.\images\善用padding.png)

当要实现这种效果时，可能会设置子盒子的marin-left和margin-top，但是当设置了子盒子的margin-top时，会导致父盒子下移了，是因为子盒子在下移的过程中，没有找到父盒子的边框线，会以标准文档流网页的最上方为边框，形成下移。

**解决方法1：**为父盒子顶端添加border

为父盒子添加边框后，子盒子就招到了下移的边框依据，以父盒子的顶端为依据下移

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        .father{
            width: 340px;
            height: 340px;
            border-top: 1px solid red;
            background-color: blue;
        }
        .box1{
            width: 200px;
            height: 200px;
            background-color: red;
            margin-left: 30px;
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <div class="father">
        <div class="box1"></div>
    </div>
</body>
</html>
```





**解决方法2：**使用父盒子的padding

**添加padding后，会使当前盒子的高度变为盒子当前的高度+padding的高度，使盒子变大，所以设置padding后，要使盒子本身的高度减去padding的高度**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        .father{
            width: 340px;
            height: 340px;
            background-color: blue;
            /* 添加padding后，会使当前盒子的高度变为盒子当前的高度+padding的高度，使盒子变大，所以设置padding后，要使盒子本身的高度减去padding的高度 */
            padding: 30px;
        }
        .box1{
            width: 200px;
            height: 200px;
            background-color: red;
        }
    </style>
</head>
<body>
    <div class="father">
        <div class="box1"></div>
    </div>
</body>
</html>
```

