is_valid是对字段进行校验的方法

return self.is_bound and not self.errors

errors中有错误，那么就是True，not self.errors就是返回False

errors中没有错误，那么就是False，not self.errors就是返回True

在errors方法中返回的是return self._errors，包含的

full_clean方法中有self._clean_fields()校验字段方法

在full_clean方法中有

self.errors=ErrorDict()存放错误信息

self.cleaned_data存放正确信息

self._clean_fields()：

​	for name, field in self.field.items()  #其中field.items表示{'username':规则对象,'password':’规则对象}，所以field就表示每个规则对象

​	value=field.clean(value)，value表示request.POST传入的post请求字典值，如{'username':'alex','password':'123456'}，按照field规则对象，校验传入的数据

如果校验成功，则会把数据放入cleaned_data[name]=value字典中

但是如果失败就会捕获ValidationError错误，就会将数据放入error字典中

成功校验后，程序判断校验类下是否有’clean_%s‘%name这个方法，有就会执行这个方法

```python
def clean_name(self):
	# 获取源码中经过第一层校验cleaned_data字典中用户输入的内容
	val=self.cleaned_data.get('name')
    
    # 使用用户输入的内容进行SQL查询
	ret=User.objects.filter(name=val)
	
    # 如果查询到数据，就直接返回数据，如果没有查询到则报异常ValidtionError异常，吻合和源码中的ValidtionError异常
	if not ret:
		return val
	else:
		raise ValidationError('该用户已注册')
```



