事件对象event

**event.currentTarget**，当前绑定匿名函数的对象

**event.target**，当前触发事件的JS对象

**event.target.value**，获取当前对象中的value值



监听input中的输入内容事件方法：

js：oninput

jquery：没有

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
    <input type="text">
    <p class="console"></p>
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        $('button').click(function(event){
            // 打印当前绑定匿名函数的对象
            console.log(event.currentTarget);
            // 打印触发事件的JS对象
            console.log(event.target);
            // 输出true，等价于this
            console.log(this === event.target);
        });
        $('body').click(function(event){
            console.log(event.currentTarget);
            console.log(event.target);
        });
        $('html').click(function(event){
            console.log(event.currentTarget);
            console.log(event.target);
        });
        
        // oninput是在JS对象中，获取input输入内容时，所触发的事件
        $('input').get(0).oninput = function(e){
            console.log(e.target.value);
            // e.target.value可以实时获取到在input中输入的内容，赋值给p标签
            $('.console').text(e.target.value);
        }
    </script>
</body>
</html>
```



