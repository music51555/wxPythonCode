**z-index**

**1、z-index值大的压着值小的**

![z-index值大](E:\workspace\wxPythonCode\Note\web框架\images\z-index值大.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        .box1{
            width: 200px;
            height: 200px;
            background-color: red;
            margin-bottom: -20px;
            position: relative;
            /* 如果都定位了，那么z-index值大的元素将压着值小的元素 */
            z-index: 1;
        }
        .box2{
            width: 200px;
            height: 200px;
            background-color: blue;
            position: relative;
            z-index: 0;
        }
    </style>
</head>
<body>
    <div class="box1">

    </div>
    <div class="box2">

    </div>
</body>
</html>
```



2、只有使用了相对定位、绝对定位、还是固定定位都可以使用z-index，**浮动元素不能使用**

3、z-index没有单位，就是一个正整数，默认为0

4、如果都没有z-index值，或者值都一样，那么谁写在HTML后面，谁压着谁

![z-index值相同](E:\workspace\wxPythonCode\Note\web框架\images\z-index值相同.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        .box1{
            width: 200px;
            height: 200px;
            background-color: red;
            margin-bottom: -20px;
            position: relative;
            /* 如果z-index的值相同，那么写在html后面的元素将压着前面的元素 */
            z-index: 1;
        }
        .box2{
            width: 200px;
            height: 200px;
            background-color: blue;
            position: relative;
            z-index: 1;
        }
    </style>
</head>
<body>
    <div class="box1">

    </div>
    <div class="box2">

    </div>
</body>
</html>
```

5、定位了元素永远压着没有定位的元素

![定位压着没定位](E:\workspace\wxPythonCode\Note\web框架\images\定位压着没定位.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        .box1{
            width: 200px;
            height: 200px;
            background-color: red;
            margin-bottom: -20px;
            position: relative;
            /* 定位后的元素压着没有定位的元素 */
            z-index: 1;
        }
        .box2{
            width: 200px;
            height: 200px;
            background-color: blue;
        }
    </style>
</head>
<body>
    <div class="box1">

    </div>
    <div class="box2">

    </div>
</body>
</html>
```





6、从父现象

如果父级元素设置z-index，那么就以父级的z-inddex为准

如果父级元素没有设置z-index，而自己设置了z-index，那么就以子级的z-index为准

用途：

![z-index覆盖](E:\workspace\wxPythonCode\Note\web框架\images\z-index覆盖.png)

例如导航栏设置了定位，下方的某个盒子也设置了定位，那么他们的默认z-index的值都是0，所以后面的盒子会在浏览网页时，会覆盖掉固定的导航栏，出现如上图的现象，所以就需要使用z-index设置值

![z-index从父现象](E:\workspace\wxPythonCode\Note\web框架\images\z-index从父现象.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        .father1{
            width: 200px;
            height: 200px;
            background-color: red;
            position: relative;
            /* 如果父级设置了z-index，那么就对比父级之间的z-index */
            z-index: 0;
        }
        .child1{
            width: 100px;
            height: 100px;
            background-color: pink;
            position: relative;
            top: 250px;
            left: 450px;
            /* 如果父级没有设置z-index，只有子级设置了z-index，那么就是子级之间的z-index进行对比 */
            z-index: 1;
        }
        .father2{
            width: 200px;
            height: 200px;
            background-color: blue;
            position: relative;
            z-index: 1;
        }
        .child2{
            width: 100px;
            height: 100px;
            background-color: green;
            position: relative;
            top: 100px;
            left: 500px;
            z-index: 0;
        }
        
    </style>
</head>
<body>
    <div class="father1">
        <div class="child1">

        </div>
    </div>
    <div class="father2">
        <div class="child2">

        </div>
    </div>
</body>
</html>
```

