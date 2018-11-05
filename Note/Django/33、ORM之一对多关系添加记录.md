ORM多表添加记录

#### 实际是对foreign key字段赋值或赋值对象

```python
from django.shortcuts import render,HttpResponse
from app01.models import Book
from app01.models import Publish

def add(request):
    # 在插入书籍信息前，首先插入一条出版社信息，因为书籍表中有出版社的外键列publish_id
    # Publish.objects.create(name='北京出版社',city='北京',email='23215412@qq.com')

    # 1、多表查询第一种插入数据方式：直接指定外键字段的值
    book_obj=Book.objects.create(title='水浒传',price=199,publishDate='2012-9-8',publish_id=1)
    print(book_obj.title)
    # 虽然没有为publish传入publish_obj，但是设置了publish_id=1，Django会为其解析为publish_id=1的publish_obj对象，其代表出版社表中id=1这条记录的对象
    print(book_obj.publish)
    print(book_obj.publish.email)

    publish_obj=Publish.objects.get(name='北京出版社')
    # 2、第二种插入数据方式，将查询出的publish_obj对象，作为外键的值传入，但在数据库的表中实际存储的是出版社的id，也就是1
    book_obj=Book.objects.create(title='三国演义',price=82,publishDate='2012-5-12',publish=publish_obj)
    print(book_obj.title)
    # 打印传入的publish_obj对象，输出Publish object (1)，因为为publish传入的就是publish_obj
    print(book_obj.publish)
    # 打印解析后的publish_id的值，也就是当前对象的id
    print(book_obj.publish_id)

    # 查询西游记这本书出版社的邮箱
    # 在通过create方法新增数据时，为publish字段传入的是publish_obj对象，publish字段对应的是创建表时指定的外键publish
    book_obj=Book.objects.get(title='西游记')
    print(book_obj.publish.email)

    return HttpResponse('OK4')
```

