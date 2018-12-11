显示Ajax提交请求的错误信息

在`ajax`的`success`返回函数中：

如果校验正确，`data`的结果是`{'user':alex,'msg':None}`

如果校验错误，`data`的结果是`{'user':None,'msg':[{'username':'error......'}...]`，存储的`errors`字典

通过`$('#id_'+data.name).next().text()`为`input`标签的下一个`span`标签设置错误信息

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



添加`error_message`实现错误描述中文化：

执行`def clean_user(self)`时表示通过了参数配置的错误校验

验证用户是否存在，如果存在会在ajax中添加html的错误信息

全局钩子，验证密码和确认密码是否一致，添加到确认密码后的span标签