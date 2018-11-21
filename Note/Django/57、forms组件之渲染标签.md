froms组件之渲染标签

在`HTML`网页中可以手写每一个标签，但是也可以通过`django`**在`HTML`页面的`get`请求中**渲染出标签，**主要的目的是有效的防止`HTML`网页中`name`的属性名与`form`类中的属性名不一致而产生的错误**



在`form`表单中通过校验类实例化出对象

```python
def register(request):
	# 在视图函数的get请求中，实例化出form对象，传入HTML网页，用于渲染form表单中的标签
    form=UserForm(request.POST)

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

通过`form.as_p`直接输出form表单，虽然很快的输出表单，但是不能调整某一个标签的样式

```html
<form action="" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>
```

