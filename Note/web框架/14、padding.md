padding的属性，方向的设置顺序是上、右、下、左

**1、小属性**

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



**3、清除一些标签中的默认padding和margin**

padding在默认的网页body、ul等标签中都是默认存在的，所以在建站时将其去除

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>

<style type="text/css">
    /* 虽然可以使用通配符选择器，但是性能差 */
    *{
        padding: 0;
        margin: 0;
    }

    /* 但是使用组合选择器，是别人总结的标签集 */
    body, div, dl, dt, dd, ul, ol, li, h1, h2, h3, h4, h5, h6, pre, code, form, fieldset, legend, input, button, textarea, p, blockquote, th, td {
    margin: 0;
    padding: 0;
    }
</style>
<body>
    
</body>
</html>
```



