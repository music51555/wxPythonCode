contentType请求头

**enctype表示请求的数据以什么格式进行编码，对应请求头中的Content-type**

#### 1、`enctype`属性**默认**为`urlencoded`类型，数据格式展示为`username=wangxin&password=123456 `

```html
<!--form表单基于urlencoded类型提交表单-->
<form action="" method="post" enctype="application/x-www-form-urlencoded">
    用户名：<input type="text" name="username">
    密码：<input type="password" name="password">
    <input type="submit" id="login">
</form>
```

视图函数`request.post`展示为：

```python
<QueryDict: {'username': ['wangxin'], 'password': ['123456']}>
```

请求头ContentType展示为：

```
Content-Type: application/x-www-form-urlencoded
```



#### 2、`enctype`属性为`form-data`类型，用于上传文件

```html
<!--用于上传文件的form表单，enctype类型为form-data-->
<form action="" method="post" enctype="multipart/form-data">
    用户名：<input type="text" name="username">
    密码：<input type="password" name="password">
    头像：<input type="file" name="pic">
    <input type="submit">
</form>
```

视图函数`request.POST`和`request.FILES`展示为：

```python
# request.POST
<QueryDict: {'username': ['wangxin'], 'password': ['123456']}>

# request.FILES
<MultiValueDict: {'pic': [<InMemoryUploadedFile: 吹头.jpg (image/jpeg)>]}>
```

请求头ContentType展示为：

```
Content-Type: multipart/form-data
```



#### 3、基于ajax发送的post请求，默认`enctype`也是以`urlencoded`类型发送数据

HTML：

```html
<body>
    用户名：<input type="text" name="username">
    密码：<input type="password" name="password">
    头像：<input type="file" name="pic">
    <button id="register">提交</button>
</body>
```

Ajax

```javascript
$(function(){
        $('#register').click(function(){
            $.ajax({
                #默认是以urlencoded类型发送请求数据
                url:'',
                type: 'post',
                data: {
                    'username':$('[name=username]').val(),
                    'password':$('[name=password]').val()
                },
                success:function(data){
                    console.log(data)
                }

            })
        })
    })
```

视图函数`request.POST`和`request.FILES`展示为：

```
<QueryDict: {'username': ['wangxin'], 'password': ['123456']}>
<MultiValueDict: {}>
```

请求头ContentType展示为：

```
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
```







