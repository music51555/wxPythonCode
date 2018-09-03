CSS的特性

**1、继承性**

inherited  美 /ɪn'hɛrɪtid/  遗传

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>CSS的特性</title>
    <style type="text/css">
        /* 为父级标签添加样式，子级会继承父级的样式 */
        /* 可以继承的属性只有color、font-*、text-*、line-*这四类文本元素，盒子元素、定位元素（浮动、绝对定位、固定定位）不能继承 */
        .father{
            font-size: 30px;
            /* background-color属性是不继承的，为div标签设置背景颜色黄色后，p标签的背景颜色也显示为了黄色，是因为p标签的默认的背景颜色是透明的 */
            background-color: yellow;
        }
        .child{
            color: red;
        }
    </style>
</head>
<body>
    <!-- p标签同时继承了father类和child类的样式，可以多级继承 -->
    <div class="father" id="box">
        <div class="child">
            <p>我是一个段落</p>
        </div>
    </div>
</body>
</html>
```



**2、层叠性**

按权重的比例选用样式

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <!-- 根据选择器的标签，按照id、类、标签的顺序统计权重比例，权重大的标签将权重小的标签层叠掉 -->
    <!-- 先统计各个样式标签的id数，如果某个样式的id数最大，那么则此样式标签的权重比例最大，则使用此样式标签 -->
    <style type="text/css">
        /* id=2 class=1 tag=2 */
        div #box2.wrap2 #box3 p{
            color: red;
        }
        
        /* id=1 class=1 tag=2 */
        /* 对于第2和第3的样式标签，id数目统计是相等的，继续统计类的数目，发现第3样式标签的类权重>第2样式标签类的权重，所以使用第3样式标签 */
        #box1 .wrap2 div p{
            color: blue;
        }

        /* id=1 class=2 tag=1 */
        .wrap1 #box2 .wrap3 p{
            color: purple;
        }
    </style>
</head>
<body>
    <!-- 先数id，再数类，最后数标签，谁的权重大，选择谁 -->
    <div id="box1" class="wrap1">
        <div id="box2" class="wrap2">
            <div id="box3" class="wrap3">
                <p>这是一个段落</p>
            </div>
        </div>
    </div>
</body>
</html>
```



先看标签有没有被选中，如果选中了，那么则对（id,class,tag）的数目进行统计，谁的权重大使用谁，**如果权重比例一样，则后来者居上**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        /* id=1 class=2 tag=1 */
        /* 对于第2和第3的样式标签，权重比例是相等的，以后定义的为准*/
        #box1 .wrap2 .wrap3 p{
            color: blue;
        }

        /* id=1 class=2 tag=1 */
        .wrap1 #box2 .wrap3 p{
            color: purple;
        }
    </style>
</head>
<body>
    <div id="box1" class="wrap1">
        <div id="box2" class="wrap2">
            <div id="box3" class="wrap3">
                <p>这是一个段落</p>
            </div>
        </div>
    </div>
</body>
</html>
```



如果没有被选中，则权重比例==0，继承样式的权重永远  **<**  选中标签的样式

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        /* id=1 class=2 tag=1 */
        /* 第2标签是继承样式，第3标签是选中样式，所以选中样式永远大于继承样式*/
        #box1 .wrap2{
            color: blue;
        }

        /* id=1 class=2 tag=1 */
        .wrap1 #box2 p{
            color: purple;
        }
    </style>
</head>
<body>
    <div id="box1" class="wrap1">
        <div id="box2" class="wrap2">
            <div id="box3" class="wrap3">
                <p>这是一个段落</p>
            </div>
        </div>
    </div>
</body>
</html>
```



如果都是继承而来的，那么权重都为0，以就近原则为准，哪个选择器对于标签描述的更近，更精确，就选择谁

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        /* id=1 class=2 tag=1 */
        /* 当都是继承而来的样式，那么以就近原则为准，谁的描述离目标样式越近，越精确，则使用谁 */
        #box1 .wrap2 .wrap3{
            color: blue;
        }

        /* id=1 class=2 tag=1 */
        .wrap1 #box2{
            color: purple;
        }
    </style>
</head>
<body>
    <div id="box1" class="wrap1">
        <div id="box2" class="wrap2">
            <div id="box3" class="wrap3">
                <p>这是一个段落</p>
            </div>
        </div>
    </div>
</body>
</html>
```



**总结：**

1、先看标签有没有被选中，如果选中了，那么则按（**id**,**class**,**tag**）的数目进行统计，谁的权重大使用谁

2、如果权重比例一样，层叠性后来者居上，后定义的样式将覆盖先定义的样式

3、如果没有被选中，则权重比例==0，继承样式的权重  **<**  选中标签的样式的权重

4、如果都是继承而来的，那么权重都为0，以就近原则为准，哪个选择器对于目标标签描述的更近，更精确，就选择谁。使用！important不影响，只影响选中的元素

5、如果描述都是一样近的，那么就需要按（**id**,**class**,**tag**）统计标签的权重了

