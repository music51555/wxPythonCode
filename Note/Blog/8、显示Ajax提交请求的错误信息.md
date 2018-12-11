显示Ajax提交请求的错误信息

在`ajax`的`success`返回函数中，data是在视图函数中设置的`msg=form.errors`：

如果校验正确，`data`的结果是`{'user':alex,'msg':None}`

如果校验错误，`data`的结果是`{'user':None,'msg':[{'username':'error......'}...]`，存储的`errors`字典

通过`$('#id_'+data.name).next().text()`为`input`标签的下一个`span`标签添加错误信息

![1544429212328](.\image\1544429212328.png)

```javascript
$('.register-btn').click(function(){
    var formdata = new FormData()

    var form_key=$('#form').serializeArray()

    $.each(form_key,function(index,data){
        formdata.append(data.name,data.value)
    })
    formdata.append('avatar',$('#avatar')[0].files[0])

    $.ajax({
        url:'',
        type:'post',
        contentType:false,
        processData:false,
        data:formdata,
        // 如果校验正确，返回的data是{'user':alex,'msg':None}
        // 如果校验错误，返回的data是
        //{
        //'user':None,
        //'msg':{
        //	'username': ['This field is required.'], 
        //	'password': ['This field is required.'], 
        //	'r_password': ['This field is required.']
        //	}
        //}，实际存储的就是form.errors字典
        success:function(data){
            // 提交一次请求后显示错误信息，输入正确后再次提交，错误信息依然显示，并没有清空，所以在添加错误信息前，先将所有字段的错误信息和has-error样式都清空
            $('.error').text('')
            $('.error').parent().removeClass('has-error')
            // 在循环data的过程中，如果data是字典，那么function(key,value)传入的是字典的key和value，每一个标签的id是id_username等，所以对每一个标签后的span进行赋值错误信息
            $.each(data.msg,function(key,value){
                // next()表示查找目标元素后面的元素
                $('#id_'+key).next().text(value)
            })
        }
    })
})
```

返回`form.errors`字典内容

![1544426704959](.\image\1544426665151.png)



在自定义的`forms`校验类中，对每一个字段，添加`error_message`实现错误描述中文化：

`error_messages`有`required`必填项检查，还有`invalid`邮箱格式校验

```python
username=forms.CharField(
    min_length=4,
    label='用户名',
    # error_messages有required必填项检查，还有invalid邮箱格式校验
    error_messages={'required':'用户名不能为空'},
    widget=widgets.TextInput(attrs={'class':'form-control'})
)
    
email=forms.EmailField(
    label='邮箱',
    error_messages={'required': '邮箱不能为空','invalid': '邮箱格式不正确'},
    widget=widgets.EmailInput(attrs={'class':'form-control'})
)
```



在自定义的`forms`校验类中，添加局部钩子校验字段

执行`def clean_username(self)`时表示通过了参数配置的错误校验

```python
# 局部钩子，校验单一字段，clean_username
    def clean_username(self):
        username=self.cleaned_data.get('username')

        user=UserInfo.objects.filter(username=username)

        if not user:
           # 如果校验数据正确，就返回数据即可
           return user
        else:
            # 当前字段报出异常后，就会存储在error字典中，当在ajax中循环时，就会将其根据id_+key.next.text存储为标签值
            raise ValidationError('用户已存在')
```



在自定义的`forms`校验类中，添加全局钩子校验密码和确认密码是否一致

```python
# 全局钩子在errors字典中的key是__all__，在ajax返回的data中获取
def clean(self):
    pwd=self.cleaned_data.get('password')
    r_pwd=self.cleaned_data.get('r_password')
	
    # 在有值的情况下再去判断两次密码是否一致，否则一个填写，一个没填写就会报字段为必填项的错误
    if pwd and r_pwd:
        if pwd==r_pwd:
            # 如果校验数据正确，就返回cleaned_data即可
            return self.cleaned_data
        else:
            # 此时报出的异常，在errors字典中，key为__all__
            raise ValidationError('两次密码不一致')
    else:
        return self.cleaned_data
```


```python
$.ajax({
    url:'',
    type:'post',
    contentType:false,
    processData:false,
    data:formdata,
    success:function(data){
        if(data.user){
            # 如果校验成功，通过location.href='/login'跳转页面
            location.href='/login'
        }else{
            $('.error').text('')
            $('.error').parent().removeClass('has-error')

            # data.msg是字典形式，key为username，value为["This field is required."]是列表
            $.each(data.msg,function(key,value){
                # 全局钩子报出的异常，key为__all__，在循环errors字典时，判断有无__all__的key，并把错误添加到确认密码下方
                if(key=='__all__'){
                    $('#id_'+'r_password').next().text(value)
                }
                # errors字典的value是一个列表，获取第一个元素错误描述
                $('#id_'+key).next().text(value[0])
                $('#id_'+key).next().parent().addClass('has-error')
            }) 
        }
    }
})
```

