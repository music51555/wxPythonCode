padding的属性，方向的设置顺序是上、右、下、左

**1、小属性**

**分别编辑padding的上（top）、右（right）、下（bottom）、左（left）属性**

bottom   美 /'bɑtəm/  底部；末端

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        div{
            width: 398px;
            height: 398px;
            border: 1px solid red;
            
            /* 前端的顺序是上、右、下、左 */
            padding-top: 20px;
            padding-right: 30px;
            padding-bottom: 40px;
            padding-left: 50px;
        }
    </style>
</head>
<body>
    <div>
        这是一堆内容这是一堆内容这是一堆内容这是一堆内容这是一堆内容这是一堆内容这是一堆内容这是一堆内容这是一堆内容这是一堆内容这是一堆内容
    </div>
</body>
</html>
```



**2、综合属性**

在一行中设置padding的上、左、下、右属性，**padding：20px 30px 40px 50px;**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        div{
            width: 398px;
            height: 398px;
            border: 1px solid red;
            
            /* 四个属性值依次表示上、右、下、左 */
            /* padding:20px 30px 40px 50px; */

            /* 三个属性值依次表示上、（左右）、下 */
            /* padding:20px 30px 20px; */

            /* 两个属性值依次表示（上下）、（左右） */
            padding:20px 30px
        }
    </style>
</head>
<body>
    <div>
        这是一堆内容这是一堆内容这是一堆内容这是一堆内容这是一堆内容这是一堆内容这是一堆内容这是一堆内容这是一堆内容这是一堆内容这是一堆内容
    </div>
</body>
</html>
```

