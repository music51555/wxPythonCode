CSS的特性

**总结：**

1、先看有没有选中被选标签层级，如果都选中了，那么按（**id**,**class**,**tag**）的数目进行统计，谁的权重大使用谁

2、如果权重比例一样，层叠性后来者居上，后定义的样式将覆盖先定义的样式

3、如果一个选中，一个没选中，则选中标签的样式的权重  **>**  继承样式的权重

4、如果都没有被选中，则权重比例==0，以就近原则为准，哪个选择器对于目标标签描述的更近，更精确，就选择谁

5、如果描述都是一样近的，那么就需要按（**id**,**class**,**tag**）统计标签的权重了

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
        /* 父级标签添加的样式，子级会继承父级的样式 */
        /* 可以继承的属性只有color、font-*、text-*、line-*这四类文本元素。像盒子元素、定位元素（浮动、绝对定位、固定定位）不能继承 */
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
    <!-- 如果某个样式的个数最大，那么则此样式标签的权重比例最大，则使用此样式标签 -->
    <style type="text/css">
        /* id=2 class=1 tag=2 */
        div #box2.wrap2 #box3 p{
            color: red;
        }
        
        /* id=1 class=1 tag=2 */
        /* 对于第2和第3的样式标签，数目统计是相等的，继续统计类的数目，发现第3样式标签的类的个数>第2样式标签类的个数，所以使用第3样式标签,如果标签的权重一样大,那么后来者居上 */
        
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
    <!-- 先数id，再数类，最后数标签，谁的权重比例大，选择谁 -->
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



1、先看标签有没有被选中，如果选中了，那么则对（id,class,tag）的数目进行统计，谁的权重大使用谁，**如果权重比例一样，则后来者居上**

2、如果没有被选中（选中：选择器使用标签选择器），则权重比例==0， 选中标签的样式  >  继承样式的权重 

3、如果都是继承而来的，那么权重都为0，以就近原则为准，哪个选择器对于标签描述的更近，更精确，就选择谁

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        /* 1、都选中标签层级的 */
        /* 先看选择器有没有选择当前要美化的标签层级的id、类、tag。如果有，则是选中状态，如果没有，则是继承状态。如下div标签都为被选中状态，此时为都选中状态，应按照id、class、tag的顺序统计权重比例*/
        /* 如果权重比例一样，则后来者居上 */
        .box div div{
            width: 100px;
            height: 100px;
            background-color: blue;
        }
        .box #wrap div{
            width: 100px;
            height: 100px;
            background-color: red;
        }

        /* 2、一个选中标签层级，一个继承样式 */
        /* 选中：选择到要美化的那一层级的id、类、标签 */
        /* 继承：没有选择到要美化的那一层级的id、类、标签 */
        /* 选中状态的权重 > 继承状态*/
        .box>div>div{
            width: 100px;
            height: 100px;
            background-color: blue;
        }
        .box #wrap{
            width: 100px;
            height: 100px;
            background-color: red;
        }

        /* 3、如下都没有选中标签层级，都为未选中状态,此时看那个选择器对于被选标签的描述更精确，更近，则使用哪个标签 */
        /* 如果描述都是一样近，那么就重新按照id、class、tag的顺序统计权重比例 */
        .box #wrap  #innerbox{
            width: 100px;
            height: 100px;
            background-color: blue;
        }

        .box>div #innerbox{
            width: 100px;
            height: 100px;
            background-color: red;
        }
    </style>
    
</head>
<body>
    <div class="box">
        <div id="wrap">
            <div id="innerbox">
                这是一个盒子
            </div>
        </div>
    </div>
</body>
</html>
```



