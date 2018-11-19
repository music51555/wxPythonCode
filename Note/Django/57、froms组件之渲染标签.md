froms组件之渲染标签

在`HTML`网页中可以手写每一个标签，但是也可以通过`django`**在`HTML`页面的`get`请求中**渲染出标签，**主要的目的是有效的防止`HTML`网页中`name`的属性名与`form`类中的属性名不一致而产生的错误**

在实例化继承于`forms.Form`的类后，通过`locals()`传入HTML网页，为每一个标签添加`label`属性，用于定义字段名称

```python
class UserForm(forms.Form):
    username=forms.CharField(min_length=4,label='用户名')
    password=forms.CharField(min_length=4,label='密码')
    email=forms.EmailField(label='邮箱')
```



并在`form`表单中渲染标签

```python
def register(request):
    form=UserForm(request.POST)

    if form.is_valid():
        print(form.cleaned_data)
    else:
        print(form.cleaned_data)
        print(form.errors)
        print(form.errors.get('password')[0])
        print(form.errors.get('email')[0])

    return render(request,'register.html',locals())
```



**渲染方式一：**通过实例化的对象.字段`form.username`来实现渲染标签

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="">
    {% csrf_token %}
    <!--form.username.label可以获取定义类时的label变量名	-->
    <p>{{ form.username.label }}：{{ form.username }}</p>
    <p>{{ form.password.label }}：{{ form.password }}</p>
    <p>{{ form.email.label }}：{{ form.email }}</p>
    <p>
        <input type="submit">
    </p>
</form>
</body>
</html>
```



**渲染方式二（推荐使用）：**循环form对象，循环的内容是每一个字段

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<from action="">
    {% for field in form %}
        <p>{{ field.label }}:{{ field }}</p>
    {% endfor %}
</from>
</body>
</html>
```



**渲染方式三：**

通过`form.as_p`直接输出form表单

```html
<form action="" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>
```

