**BOM**

**open**

**close**

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
    <button>新浪</button>
    <script type="text/javascript">
        var btn = document.getElementsByTagName('button')[0];
        btn.onclick  = function(){
            // 默认从新的标签页打开，添加'_self'参数后，从当前标签也打开
            window.open('https://www.sina.com.cn/','_self');
            // 关闭标签页
            window.close();
        }
    </script>
</body>
</html>
```



**window.location**

window.location方法提供了很多属性

![location](.\location.png)



```html
/*
hash: url参数中的哈希值
host: 主机地址 www.baidu.com
hostname: 主机名称 www.baidu.com
search: 当在百度搜索内容后，该参数变为搜索的URL
*/
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <button>新浪</button>
    <script type="text/javascript">
        var btn = document.getElementsByTagName('button')[0];
        setTimeout(function(){
            // 通过调用location的href属性，将地址转换
            location.href = 'https://www.baidu.com';
        },3000);
    </script>
</body>
</html>
```



**history模式**

前进：**history.go(1);** 

后退：**history.go(-1);**

刷新：

**1、history.go(0);**

**2、window.location.reload();**

history前进、后退后网址变为history模式被存储起来，局部刷新使用ajax

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
    <a href="./index.html">百度</a>
    <button id="forward">前进</button>
    <button id="back">后退</button>
    <button id="refresh">刷新</button>
    <script type="text/javascript">
        alert(1);
        var forward = document.getElementById('forward');
        var back = document.getElementById('back');
        var refresh = document.getElementById('refresh');

        forward.onclick = function(){
            window.history.go(1);    
        }
        
        back.onclick = function(){
            window.history.go(-1);
        }

        refresh.onclick = function(){
            //通过window.history.go(0)刷新
            window.history.go(0);
            
            //通过window.location.reload()刷新
            window.location.reload();
        }
    </script>
</body>
</html>
```





