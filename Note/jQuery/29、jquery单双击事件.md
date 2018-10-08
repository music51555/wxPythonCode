jquery单双击事件

**click：**单击事件

**dblclick：**双击事件

**clearTimeout：**清除定时器

单击、双击的时间差是300毫秒



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
    <button>按钮</button>
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        var timer = null;
        // 单击时触发的事件
        $('button').click(function(){
            clearTimeout(timer);
            timer = setTimeout(function(){
                console.log('单击了');
            },301);
        });

        // 双击时触发的事件，但是在触发双击事件时，会触发两次单击事件，如何阻止两次单击事件的发生呢？单击和双击的时间差是300毫秒，在设置定时器后，只是延迟了单击事件的触发事件，但是并没有真正阻止单击事件的发生，所以可以在触发双击事件时，清除单击事件中的定时器，但是清除后，仍然执行了一次单击事件的发生，是因为在双击时，走到单击事件的发生时，第一次按照代码由上至下的执行顺序，总会执行一次单击事件，所以在单击事件定时器执行前，再清除一次定时器
        $('button').dblclick(function(){
            clearTimeout(timer);
            console.log('双击了');
        });
    </script>
</body>
</html>
```

