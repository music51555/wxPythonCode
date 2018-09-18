事件

**onclick**

**onload**

**触发事件，并绑定匿名函数**

window.onload = function(){

}

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>

    <style type="text/css">
        #box1{
            width: 100px;
            height: 100px;
            background-color: red;
        }
    </style>
</head>
<body>
    <div id="box1" class="box"></div>
    <div id="box2" class="box"></div>
    <script type="text/javascript">
        // 入口函数，window.onload()
        // 在等待整个文档和图片资源加载完成之后会触发onload事件，将onload方法绑定一个匿名函数
        window.onload = function(){
            alert('page load finish');
        };

        // 覆盖现象,，如果写了多个window.onload，那么第2个会覆盖第1个
        // 1、JS触发事件，直接绑定匿名函数，常用
        window.onload = function(){
            alert('documen load finish');
            // 1、获取事件源
            var divobj = document.getElementById('box1');
            // 2、触发事件
            divobj.onclick = function(){
                // 3、事件驱动
                alert('clicked');
            }
        };
        
        // 2、先定义函数名，再实现函数
        var divobj = document.getElementById('box1');
        divobj.onclick = fn;
        function fn(){
            alert(1);
        }
    </script>
</body>
</html>
```

