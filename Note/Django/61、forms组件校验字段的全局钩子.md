再次查看full_clean方法中的_clean_form方法，其中

cleaned_data=self.clean()方法是全局钩子，他是隶属于BaseForm的类的，而我们定义的UserForm类是继承与forms.Form的，所以在校验类中定义clean方法是重写父类的方法

校验完毕后，如果校验真确，源码中return cleaned_data，那么在clean方法中也return cleaned_data

如果校验失败，源码

except ValidationError:

​	self.add_error(None,e) 这是没有为错误描述执行key，因为他是一个全局错误，{'_ _all_ _':[e,]}，所以在clean方法中也要捕获ValidationError异常

```python
def clean(self):
	pwd=self.cleaned_data.get('pwd')
	r_pwd=self.cleaned_data.get('r_pwd')
	
	if pwd==r_pwd:
		return cleaned_data
	else:
		raise ValidationError('两次密码不一致')
```

如果此时写完，去HTML表单进行验证，此时无法显示出全局错误，因为在源码中是self.add_error(None,e)，没有任何键值，所以在HTML中{{ form.username.error.0 }}无法输出错误描述



在post请求中打印

print(form.errors.get('_ ___all_ _ _')[0])输出全局错误

error=form.errors.get('_ ___all_ _ _')将变量传入到HTML网页，通过{{ error.0 }}打印错误

class=error颜色变红



当密码位数不足，且两次密码不一致时，

先执行full_clean方法中的_clean_fields方法进行单一的字段校验，此时由于密码规则没有匹配成功，将字段key传入了errors字典，继续执行_clean_form中的clean全局钩子方法，相互比较时，得不到pwd字段的值，就是None，所以也会报两次密码不一致的错误

逻辑应该是在两个字段基础规则校验通过的基础上，再去校验两次密码是否一致，所以在全局钩子加

if pwd and r_pwd:

​	再去校验

else:

​	return cleaned_data



将forms代码放入单独的myform.py文件中，在视图函数中再引入，解耦合