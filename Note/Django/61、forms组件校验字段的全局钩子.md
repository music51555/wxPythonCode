**全局钩子可以同时校验多个字段之间的交互规则**，如密码和确认密码

```python
#源码中self.clean方法是全局钩子函数
def _clean_form(self):
	try:
		cleaned_data = self.clean()
	except ValidationError as e:
		self.add_error(None, e)
	else:
		if cleaned_data is not None:
			self.cleaned_data = cleaned_data
```

但在方法中只`return self.cleaned_data`，没有代码逻辑

```python
    def clean(self):
     
        return self.cleaned_data
```



clean方法隶属于`class BaseForm`类

```python
class BaseForm:
   def clean(self):
        return self.cleaned_data
```

自定义的校验类`RegisterForm`继承于`forms.Form`

```python
class RegisterForm(forms.Form):
    pass
```

`Form`类继承于`BaseForm`类：

```python
class Form(BaseForm, metaclass=DeclarativeFieldsMetaclass):
    pass
```

所以，可以在`RegisterForm`中重写`clean`方法

```python
    def clean(self):
        pwd=self.cleaned_data.get('password')
        r_pwd=self.cleaned_data.get('r_password')

        # 如果校验成功规则对象中的规则，如min_length=4,或clean_%s中的规则，如clean_password、clean_r_password，那么他们会被存储在cleaned_data字典中，否则就会在errors字典中，所以先从cleaned_data中查询出两个校验成功的字段值，如果可以查询出两个字段，再进行校验
        if pwd and r_pwd:
            if pwd==r_pwd:
                # 与源码信息一致，正确返回self.cleaned_data
                return self.cleaned_data
            else:
                raise ValidationError('两次密码不一致')
```

此时写完代码，在HTML表单中无法报出错误，因为在源码中：

```python
    def _clean_form(self):
        try:
            cleaned_data = self.clean()
        except ValidationError as e:
            # 在源码中将错误描述添加到了一个None中，实际获取错误描述的key是__all__
            self.add_error(None, e)
```



如果此时写完，去HTML表单进行验证，此时无法显示出全局错误，因为在源码中是将错误描述e，添加到没有键值的None，所以在HTML中`{{ form.username.error.0 }}`无法根据指定key输出错误描述，所以可以在post请求中打印`print(form.errors.get('_ _all_ _')[0])`来输出全局错误

```python
if form.errors.get('__all__'):
    error=form.errors.get('__all__')[0]
```





