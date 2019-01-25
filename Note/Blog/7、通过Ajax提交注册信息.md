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
           	 // 如果校验正确，返回的data是{'user':alex,'msg':None}
        	// 如果校验错误，返回的data是{'user':None,'msg':{'username': ['This field is required.'], 'password': ['This field is required.'], 'r_password': ['This field is required.']}}，实际存储的就是form.errors字典
                success:function(data){
                    console.log(data)
                }
            })
        })
    })
```



**视图函数：**

**知识点1：**`request.is_ajax()`表示是通过`ajax`的请求

**知识点2：**创建`form`对象，并传入`request.POST`数据后，调用`form.is_valid`来验证请求数据

**知识点3：**从`form.cleaned_data.get`中获取正确数据集

**知识点4：**从`form.errors`中获取错误数据集

```python
def register(request):

    response={'user':None,'msg':None}

    if request.is_ajax():
        form=myForms.UserForm(request.POST)

        if form.is_valid():
            # 如果校验成功，则在正确数据集的cleaned_data中获取校验正确的用户名
            response['user']=form.cleaned_data.get('username')

            return JsonResponse(response)
        else:
            response['msg']=form.errors

            return JsonResponse(response)

    form=myForms.UserForm()
    return render(request,'register.html',locals())
```



**`formdata`提交数据优化：**

相比于之前的`formdata.append('username',$('#id_username').val())`，调用form标签下的`serializeArray`方法，返回一个列表`[{name: "username", value: "alex"},{name: "password", value: "123456"},{},{...}]`

```javascript
$('.register-btn').click(function(){
    // 创建form对象
    var formdata = new FormData()

    // serializeArray方法只能在form标签下使用，获取form标签下的每一个字段，形成一个列表[{name:username,value:alex},{name:password,value:xxx},{...}]，美 /'sɪrɪəlaɪz/ 连载，使连续
    var form_key=$('#form').serializeArray()

    // 通过$.each(form_key，function(index,data){})方法循环列表，并执行function函数,form_key的结果是列表，所以循环式可以在function中传入index和data，会显示列表每一条记录的索引和每一个索引对应的列表元素，元素data是字典，如果form_key的返回结果是字典的话，那么在function中传入(key,value)展示的是返回字典的key和value
    $.each(form_key,function(index,data){
        formdata.append(data.name,data.value)
    })

    // 除去特殊的头像值
    formdata.append('avatar',$('#avatar')[0].files[0])

    $.ajax({
        url:'',
        type:'post',
        contentType:false,
        processData:false,
        data:formdata,
        success:function(data){
            console.log(data)
        }
    })
})
```
