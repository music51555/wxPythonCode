ORM之模糊查询

**在`filter()`方法中**添加模糊查询，支持`__gt`、`__lt`、`__year`、`__month`、`__startswith`、`contains`、`in`

```python
from django.shortcuts import render,HttpResponse
from app01.models import Book

def filter_search(request):
    # __gt表示大于，__lt表示小于，也可以结合使用，查询区间范围之内的数据
    # 在models.py模块中添加了def __str__(self)： return self.title的函数，所以在打印queryset数据类型时，会对象的书名
    ret=Book.objects.all().filter(price__gt=100,price__lt=150)
    print(ret)

    # __startswith表示查找以什么开头的数据
    ret=Book.objects.filter(title__startswith='J')
    print(ret)

    # contains表示查询包含什么的数据
    ret=Book.objects.filter(title__contains='入门')
    print(ret)

    # icontains表示忽略大小写，查找包含什么的数据
    ret = Book.objects.filter(title__icontains='java')
    print(ret)

    # in表示在取值返回之内的数据
    ret=Book.objects.filter(price__in=[90,150])
    print(ret)

    # 针对日期类型的数据，支持__year,__month等模糊查询
    ret=Book.objects.filter(pub_date__year=2011,pub_date__month=10)
    print(ret)
    return HttpResponse('OK')
```

