**margin塌陷**	

当**垂直方向**的盒子分别设置了margin-bottom 30px和margin-top 50px，那么生效的margin以较大值为准，导致上方盒子的margin掉入到了下方盒子的margin中

![margin塌陷效果](E:\workspace\wxPythonCode\Note\web框架\images\margin塌陷效果.png)



然后将子盒子都设置为浮动状态，后再次查看margin之间的宽度，会发现塌陷效果没有了，所以塌陷效果对于浮动的盒子是无效的

![margin塌陷效果1](E:\workspace\wxPythonCode\Note\web框架\images\margin塌陷效果1.png)



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        /* 为父盒子设置宽度后，当子盒子设置了浮动，但父级的宽度容不下这些浮动的元素并排显示时，那么浮动的盒子就会被挤到下面 */
        .father{
            width: 400px;
        }
        .box1{
            width: 200px;
            height: 100px;
            background-color: red;
            margin-bottom: 30px;
            float: left;
        }
        .box2{
            width: 300px;
            height: 200px;
            background-color: yellow;
            margin-top: 50px;
            float:left;
        }
    </style>
</head>
<body>
    <div class="father">
        <div class="box1"></div>
        <div class="box2"></div>
    </div>
</body>
</html>
```

