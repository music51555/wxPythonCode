**jquery事件流**

在jquery中没有捕获事件流

### propagation 美 /,prɑpə'geʃən/  传播

### prevent 美 /pri'vɛnt/ 阻止

**event.stopPropageation**，简便写法return false

**event.preventDefault**，阻止a标签的默认事件，alert

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        .box{
            width: 100px;
            height: 100px;
            background-color:red;
        }
    </style>
</head>
<body>
    <div class="box">
        <button>你好</button>
        <a href="https://www.baidu.com">百度一下</a>
    </div>
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        // 当点击了盒子中的按钮时，触发了点击按钮的事件，但是又随之触发了按钮所在盒子的点击事件，这种现象成为事件冒泡
        $('button').click(function(event){
            alert('点击了按钮');
            // /,prɑpə'geʃən/  传播；繁殖，阻止事件冒泡的方法stopPropagation()
            event.stopPropagation();
            // 简洁的阻止事件冒泡的方法
            // return false;
        });
        $('a').click(function(event){
            // 点击a标签后会跳转到指定的网址，这也是一个事件，所以可以通过preventDefault()方法，阻止默认事件
            event.preventDefault();
            alert('点击了a标签');
            event.stopPropagation();
        });
        $('.box').click(function(){
            alert('点击了父盒子');
        });
    </script>
</body>
</html>
```

