jquery鼠标移入和移出事件

**mouseover：**鼠标移入父元素和子元素时，**都**会触发的方法

**mouseout：**  鼠标移出父元素和子元素时，**都**会触发的方法



**mouseenter：只有**鼠标进入被选元素时才会触发

**mouseleave：只有**鼠标离开被选元素时触发



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
            width: 100px;
            height: 100px;
            background-color: red;
        }
        .child{
            width: 50px;
            height: 50px;
            background-color: green;
        }
    </style>
</head>
<body>
    <div class="father">
        <div class="child">

        </div>
    </div>
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        // 鼠标移入或移出父元素和子元素时，都会触发的方法
        $('.father').mouseover(function(){
            console.log('移入了');
        });

        $('.father').mouseout(function(){
            console.log('移出了');
        });
            
        // 只有在进入或离开指定的元素时，才会触发的方法
        $('.father').mouseenter(function(){
            console.log('进入了');
        });
        $('.father').mouseleave(function(){
            console.log('离开了');
        });
    </script>
</body>
</html>
```



jquery的**hover**方法合成了mouseenter和mouseleave方法

实例：小米商城购物车的效果

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        *{
            padding: 0;
            margin: 0;
        }
        .father{
            width: 100px;
            height: 50px;
            background-color:red;
        }
        .child{
            width: 300px;
            height: 200px;
            background-color: green;
            position: absolute;
            top: 50px;
        }
    </style>
</head>
<body>
    <div class="father">
        <span>购物车</span>
        <div class="child" style="display:none">

        </div>
    </div>
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        // 如果使用mouseover和mouseout事件，那么是在移入和移出父级元素和子级元素都会触发事件，也就是鼠标移入父盒子和子盒子时，都会触发子盒子的slideDown方法，导致从父盒子移动到子盒子的过程中，子盒子执行了mouseout方法
        $('.father').mouseover(function(){
            $('.child').slideDown(500);
        });
        
        $('.father').mouseout(function(){
            console.log(1);
            $('.child').slideUp(500);
        });

        // 而使用mouseenter和mouseleave方法时，只有在进入和离开父盒子的时候，才会触发事件
        $('.father').mouseenter(function(){
            $('.child').stop().slideDown(1);
        });
        
        $('.father').mouseleave(function(){
            console.log(1);
            $('.child').stop().slideUp(1);
        });
            
        // jquery中的hover方法，同时集成了mouseenter方法和mouseleave方法
        $('.father').hover(function(){
            $('.child').slideDown(500);
        },function(){
            $('.child').slideUp(500);
        });
    </script>
</body>
</html>
```

