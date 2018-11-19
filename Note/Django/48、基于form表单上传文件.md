Ajax上传文件

**基于form表单的上传文件**

HTML文件：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <!--没有填写form表单的action地址，默认使用的是当前浏览器的地址-->
    <!--如果没有添加enctype="multipart/form-data"，那么在视图函数中request.FILES将获取不到任何内容-->
    <form action="" method="post" enctype="multipart/form-data">
        用户名<input type="text" name="username">
        头像 <input type="file" name="upload">
        <input type="submit">
    </form>
</body>
</html>
```



视图函数：

```python
def upload(request):
    if request.method == 'POST':
        # 输出<MultiValueDict: {'upload': [<InMemoryUploadedFile: 拆分文件.png (image/png)>]}>
        print(request.FILES)
        # 通过HTML上传文件input标签的name属性，得到文件对象，打印文件对象输出文件名
        file_obj=request.FILES.get('upload')
		
        # 循环通过request.FILES.get()获取到的文件对象，写入通过wb模式打开的文件
        with open(file_obj.name,'wb') as f:
            for line in file_obj:
                f.write(line)

    return render(request,'upload.html')
```

