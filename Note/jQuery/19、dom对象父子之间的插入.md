dom对象之间的插入

**父子之间**

**父元素添加子元素，插入到子集的最后**

**父.append(子)：**

1、字符串

2、标签+文本

3、插入JS对象

4、插入Jquery对象



**子元素添加父元素**

**(子).appendTo(父)**;



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div class="box"></div>
    <div id="wrap">
        <p>hello world</p>
    </div>
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        // 1、在标签下添加文本内容，变为<div class="box">alex</div>
        $('.box').append('alex');
        
        // 2、在标签下添加标签+文本    
        $('.box').append('<p>we are friends</p>');
        
        var input = document.createElement('input');
        input.type = 'text';
        input.placeholder = '请输入用户名';
        
        // 3、在标签下添加JS对象
        $('.box').append(input);
        
        // 4、在标签添加jquery对象，相当于把现有的jquery对象移动位置，并且连同jquery下的标签一同移动
        $('.box').append($('#wrap'));
        
        // 链式编程
        // 将子元素添加到父元素下后执行click事件
        $('<p>你好</p>').appendTo('.box').click(function(){
            $(this).css({
                width: '100px',
                height: '100px',
                background: 'red'
            });
        });
    </script>
</body>
</html>
```





**父元素添加子元素，插入到子集的开头**

**父.prepend(子)**

**子.prepengTo(父)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <ul>
        <li>alex</li>
    </ul>
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        // 父元素添加子元素、标签到子集的开头
        $('ul').prepend('<li>wxx</li>');
        
        // 子元素插入到指定父元素的开头
        $('<li>egon</li>').prependTo($('ul')).click(function(){
            alert(1);
        });
    </script>
</body>
</html>
```























