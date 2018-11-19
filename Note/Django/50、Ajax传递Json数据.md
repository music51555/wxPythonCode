Ajax传递Json数据

将Ajax中的Object类型以json的形式发送数据：序列化为字符串发送给python，在python中反序列化为字典的形式后使用

```javascript
<script type="text/javascript">
    $(function(){
        $('#register').click(function(){
            $.ajax({
                url:'',
                type: 'post',
                {#将数据类型指定以json的格式发送数据#}
                contentType:'application/json',
                {#那么此时发送的数据就要序列化为字符串后发送，使用JSON.stringify#}
                data: JSON.stringify({
                    username:$('[name=username]').val(),
                    password:$('[name=password]').val()
                }),
                success:function(data){
                    console.log(data)
                }
            })
        })
    })
</script>
```



AJax发送的json类型数据，在视图函数中是接收在`request.body`中的：

```python
# 得到的是bytes类型，如果想要使用，将其反序列化为json类型
b'{"username":"wangxin","password":"123456"}'

# 反序列化，得到dict类型，{'username': 'wangxin', 'password': '123456'}
userinfo=json.loads(request.body)

# 只有在使用默认的ContentType: urlencoded类型时，request.POST才有数据
<QueryDict: {}>
```



请求头中的`ContentType`展示为：

```
Content-Type: application/json
```

请求头中的数据展示为：

```json
{username: "wangxin", password: "123456"}
password:"123456"
username:"wangxin"
```

