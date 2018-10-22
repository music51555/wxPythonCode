**background-image**

**平铺设置背景图**

添加背景图，使用url参数名，才能正确获取到图片，**当盒子的宽度和高度大于图片的宽高时，图片会平铺重复显示**。repeat表示默认重复，no-repeat表示不重复显示背景图，repeat-x表示x轴重复，y表示y轴重复

**在为网站设置背景图时，在body标签中使用background-image: url(xxx)即可**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        .imgbox{
            width: 1200px;
            height: 1200px;
            /* 添加背景图，使用url参数名，才能正确获取到图片，当盒子的宽度和高度大于图片的宽高时，图片会平铺重复显示。repeat表示默认重复，norepeat表示不重复显示背景图，repeat-x表示x轴重复，y表示y轴重复 */
            background-image: url(./images/homesmall2.png);
            /* background-repeat: repeat;
            background-repeat: no-repeat; */
            background-repeat: repeat-x;
            /* 设置padding后，padding的区域也会显示图片，相当于图片又延伸了一点 */
            padding: 100px;

        }
    </style>
</head>
<body>
    <div class="imgbox">

    </div>
</body>
</html>
```



**background-position**

**位移图片**

如果有一张雪碧图，我们可以使用background-image：url(xxxx)添加图片后，设置background-repeat：no-repeat设置为不重复显示，通过background-position(x轴距离 y轴距离)来调整图片的位置，图片所在盒子的高度要设置为图片的高度，在完整获取图片

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        .imgbox{
            width: 1200px;
            height: 1200px;
            background-image: url(./images/homesmall2.png);
            background-repeat: no-repeat;
            /* background-position属性表示向下和向右偏移图片 */
            background-position: 100px 100px;
            /* 当为负数时，表示向左和向上偏移 */
            background-position: -100px -100px;
            /* 水平方向有三种left center right */
            /* 垂直方向有三种top center bottom，水平和垂直方向的定位搭配使用 */
            /* center center表示水平和垂直都居中，在网页的正中心 */
            background-position: center center;
            background-position: center top;
        }
    </style>
</head>
<body>
    <div class="imgbox">

    </div>
</body>
</html>
```



**background-attchment**

attachment   美 /ə'tætʃmənt/ 附件

固定图片，图片被固定在一个位置，不随着浏览器的上下浏览而移动

**CSS雪碧** 即[CSS Sprite](https://baike.baidu.com/item/CSS%20Sprite)，也有人叫它CSS精灵，是一种CSS图像合并技术，该方法是将小图标和背景图像合并到一张图片上，然后利用css的背景定位来显示需要显示的图片部分

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        .imgbox{
            width: 1200px;
            height: 1200px;
            /* 使用综合属性添加背景图片，依次设置了图片的路径，background-repeat，backg-position */
            background: url(./images/homesmall2.png) no-repeat 0 0;
            /* 固定图片，图片被固定在一个位置，不随着浏览器的上下浏览而移动 */
            background-attachment: fixed;
            color: blue;
        }
    </style>
</head>
<body>
    <div class="imgbox">
        <p>一些内容</p>
        <p>一些内容</p>
        <p>一些内容</p>
        <p>一些内容</p>
        <p>一些内容</p>
        <p>一些内容</p>
        <p>一些内容</p>
        <p>一些内容</p>
        <p>一些内容</p>
        <p>一些内容</p>
        <p>一些内容</p>
        <p>一些内容</p>
        <p>一些内容</p>
        <p>一些内容</p>
        <p>一些内容</p>
        <p>一些内容</p>
        <p>一些内容</p>
        <p>一些内容</p>
        <p>一些内容</p>
    </div>
</body>
</html>
```