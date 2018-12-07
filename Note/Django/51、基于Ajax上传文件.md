基于Ajax上传文件

```javascript
<script type="text/javascript">
    $(function(){
        $('#register').click(function(){
            {#写在JS事件中，如果写在外面视图函数将接收不到任何参数#}
            {#之所以用formdata，是因为要发送文件数据#}
            var formdata = new FormData();
            {#将发送的数据和文件以formdata.append(key，value)的形式添加#}
            formdata.append("username",$('[name=username]').val());
            formdata.append("password",$('[name=password]').val());
            {#jquery对象[0]获取JS对象.files[0]在列表中获取文件对象#}
            formdata.append("pic",$('[name=pic]')[0].files[0]);
            $.ajax({
                url:'',
                type: "post",
                {#如果不添加如下两句，将会报错Uncaught TypeError: Illegal invocation，分别表示不对数据进行编码，和不做预处理#}
                contentType:false,
                processData:false,
                {#数据仍然是通过Ajax发送出去#}
                data: formdata,
                success:function(data){
                    console.log(data)
                }
            })
        })
    })
</script>
```

在视图函数中打印`request.POST`和`request.FILES`

```
<QueryDict: {'username': ['wangxin'], 'password': ['123456']}>
<MultiValueDict: {'pic': [<InMemoryUploadedFile: 吹头.jpg (image/jpeg)>]}>
```



```python
def upload(request):

    if request.method == 'POST':
        print(request.POST)
        # 通过request.FILES.get(HTML中上传文件的name)获取文件对象
        file_obj=request.FILES.get('pic')
        with open(file_obj.name,'wb') as f:
            for line in file_obj:
                f.write(line)

    return render(request,'upload.html')
```

