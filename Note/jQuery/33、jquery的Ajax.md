jquery的Ajax

异步的JavaScript和XML，可以从服务器上请求文本、HTML、XML或JSON，可以把这些数据载入到网页的元素中

Asynchronous Javascript and XML  美 /e'sɪŋkrənəs/  异步的

动态页面：**在不重载整个网页的情况下，Ajax通过后台加载数据，显示在网页上**



常用的架构模式：

**MVC：Model View Controller**

**数据  视图  控制器，用数据驱动视图**

通过传入的不同数据，在HTML网页上显示不同的视图，因为传入的数据不同，所以显示的内容不同，控制器是方法，如text()：

```
// 根据name变量传入的数据不同，在HTML中显示的内容就不同，所以是数据驱动视图
// 控制器是text()方法，是通过text()方法来实现传入数据的
var name = 'alex'
$('p').text(name);
```



### Ajax的get请求：

**jquery的ajax方法：$.ajax({})**

**url：**请求的网址

**type：**请求的方式

**dataType：**数据类型，支持xml、html、json、javascript

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
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        $(function(){
            $.ajax({
                // 简单的ajax请求，请求的网址、访问的类型，访问成功或错误后执行的函数
                url: 'http://localhost:8880/',
                type: 'get',
                // 在success的匿名函数形参中，会得到后台返回的data数据
                success: function(data){
                    // 当访问成功根目录/后，后台response会一个data数据，是一个h2字符串标签，并将他添加到body下，展示在网页中，实现了MVC数据驱动视图，data就是服务器返回的数据，通过html方法驱动视图，展示在页面中
                    console.log(data);
                    $('body').html(data);
                },
                error: function(){
                    console.log(err);
                }
            })
            
            $.ajax({
                url: 'http://localhost:8880/course',
                type: 'get',
                // 通过后台返回的数据是字符串格式，设置数据类型为json后，变为{name: "张三"}
                dataType: 'json',
                success: function(data){
                    console.log(data);
                    // 获取到name的值，将其通过MVC赋值给jquery对象
                    $('.box').text(data.name);
                },
                error: function(err){
                    console.log(err)
                }
            });
        })
    </script>
</body>
</html>
```



### Ajax的post请求：

在post请求中，在前端为后台传递了json数据，后台将数据以json的格式存储在了列表中

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
    <form action="">
        <input type="text">
        <input type="submit" value="提交">
    </form>
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        $(function(){
            
            $('form').submit(function(event){
                // 阻止点击提交按钮后的默认事件，如果不阻止，那么不会通过ajax访问后台链接地址
                event.preventDefault();
                var name = $('[type = text]').val();
                console.log(name);
                $.ajax({
                    url: 'http://localhost:8880/create',
                    //请求方式为post，并通过json数据给后台传递数据
                    type: 'post',
                    data: {
                        "name": name
                    },
                    success: function(data){
                        console.log(data);
                    },
                    error: function(err){
                        console.log(err);
                    }
                });
            });
        });
    </script>

</body>
</html>
```

