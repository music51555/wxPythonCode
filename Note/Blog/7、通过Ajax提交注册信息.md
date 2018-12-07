通过Ajax提交注册信息

**知识点1：**通过`Formdata`类实例化`formdata`对象

**知识点2：**`formdata.append(key,value)`

**知识点3：**不要忘记通过`ajax`传输`csrfmiddlewaretoken`的值，并在`html`网页中添加`{%  csrf_token %}`

**知识点4：**如果只用`ajax`传输文件，那么就要添加`contentType:false`和`processData:false`

```javascript
$(function(){
        $('.register-btn').click(function(){
            // 之所以用formdata，是因为要通过Ajax发送上传的文件信息
            var formdata = new FormData()
            
            // append(name,jquery获取的标签值)
            formdata.append('username',$('#id_username').val())
            formdata.append('password',$('#id_password').val())
            formdata.append('r_password',$('#id_r_password').val())
            formdata.append('email',$('#id_email').val())
            
            // 调用jquery对象的JS对象.files[0]获取文件对象
            formdata.append('avatar',$('#avatar')[0].files[0])
            // 不紧要传递csrfmiddlewaretoken的值，还要在html代码中添加csrf_token的标识
            formdata.append('csrfmiddlewaretoken',$('[name=csrfmiddlewaretoken]').val())

            $.ajax({
                url:'',
                type:'post',
                // 如果不添加如下两句，将会报错Uncaught TypeError: Illegal invocation，分别表示不对数据进行编码，和不做预处理
                contentType:false,
                processData:false,
                data:formdata,
                success:function(data){
                    console.log(data)
                }
            })
        })
    })
```



**视图函数：**

**知识点1：**`request.is_ajax()`表示是通过ajax的请求

**知识点2：**创建`form`对象，并传入`request.POST`数据后，调用`form.is_valid`来验证数据

```python
def register(request):

    response={'user':None,'msg':None}

    if request.is_ajax():
        form=myForms.UserForm(request.POST)

        if form.is_valid():
            response['user']=request.POST.get('username')

            return JsonResponse(response)
        else:
            response['msg']=form.errors

            return JsonResponse(response)

    form=myForms.UserForm()
    return render(request,'register.html',locals())
```

