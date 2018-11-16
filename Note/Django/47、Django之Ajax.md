Django之Ajax

Asynchronous Javascript And XML：异步Javascript和XML

**请求的方式**

1、浏览器地址栏的get请求

2、form表单的get和post请求

3、a标签的get请求

4、Ajax发送请求



**Ajax的特点：**

1、异步请求

```
同步请求：客户端发出一个请求后，需要等待服务器响应结束后才能发送第二个请求
异步请求：客户端发出一个请求后，无需等待服务器响应结束，直接发送第二个请求
```



2、局部刷新

如博客园的注册页，用户输入内容后，可以即时获知*名称已经被使用*

![1542247241825](.\images\ajax局部刷新)



**简单的AjaxDemo**：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <button class="Ajaxbtn">Ajax</button>
</body>
<script type="text/javascript" src="/static/js/jquery-3.3.1.js"></script>
<script type="text/javascript">
    $(function() {
        {#通过Ajax向服务器发送请求，根据访问路径，得到了服务器该路径视图函数中的return数据，通过jquery将其添加到页面中，实现了局部刷新#}
        $('.Ajaxbtn').click(function () {
            $.ajax({
                {#填写跳转路径，如果没有写路径和端口，就以当前浏览器路径为准#}
                url: /test_ajax/,
                type: 'get',
                {#data是服务器返回的数据，也就是访问路径视图函数中return的内容#}
                success: function (data) {
                    console.log(data)
                    $('button').parent().append('<p>data</p>')
                }
            })
        })
    })
</script>
</html>
```



**传递参数的Ajax的Demo：**

在HTML网页中计算和

```html
<script type="text/javascript">
    $(function() {
        {#通过Ajax向服务器发送请求，根据访问路径，向服务器发送了data中Object的n1和n2属性，在视图函数中得到return数据，通过jquery将其添加到页面中，实现了局部刷新#}
        $('#cal').click(function(){
            $.ajax({
                url:'/cal/',
                type:'post',
                data:{
                    'n1':$('#num1').val(),
                    'n2':$('#num2').val()
                },
                {#Ajax函数执行成功后，会执行success函数，将结果赋值给对应标签#}
                success:function(data){
                    $('#ret').val(data)
                }
            })
        })
    })
</script>
```



```python
#视图函数
def cal(request):
    n1=int(request.POST.get('n1'))
    n2=int(request.POST.get('n2'))

    ret=n1+n2
    print(ret)

    # 通过HttpResponse返回的数据，会在jquery的success函数中，被data参数接收到
    return HttpResponse(ret)
```



通过Ajax登录验证的Demo

```javascript
#jquery
#点击登录按钮后，通过ajax的post请求，向login路径的地址发送请求，通过jquery获取用户名和密码的值，通过ajax发送到服务器，在服务器视图函数中request.POST.get解析用户名和密码，通过ORM执行SQL语句，验证输入的用户名和密码是否正确，当返回值是一个字典的时候，两个编程语言间传递json参数时，需要先dumps序列化为字符串后才能传递，在HTML中通过JSON.parse反序列化为Object类型，判断是否登录成功和失败
$('#login').click(function(){
            $.ajax({
                url:'/login/',
                type:'post',
                data:{
                    'username':$('#username').val(),
                    'password':$('#password').val()
                },
                success:function(data) {
                    ret=JSON.parse(data)
                    if(ret.username){
                        $('#error').html('<p id="status">登录成功</p>').css({'color':'green','margin-left':'5px'})
                    }else{
                        $('#error').html(ret.message).css({'color':'red','margin-left':'5px'})
                    }
                }
            })
        })
```



```python
#视图函数
def login(request):

    username=request.POST.get('username')
    password=request.POST.get('password')

    ret={"username":None,"message":None}
    user_obj=User.objects.filter(Q(username=username)&Q(password=password))
    if user_obj:
        ret['username']=username
    else:
        ret['message']='username or password wrong!'

    import json
    jsonret=json.dumps(ret)

    return HttpResponse(jsonret)
```





在Django建表时，会遇到如下问题，此时在数据库的`django_migrations`表中，清除当前应用的名称后重新创建表即可

```
Operations to perform:
  Apply all migrations: admin, app01, auth, contenttypes, sessions
Running migrations:
  No migrations to apply.
```

