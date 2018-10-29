ORM添加表记录

![ORM对应关系](./images/ORM对应关系.png)

sql中的表 <==对应==> python中的类

sql中的表记录 <==对应==> python中的类对象



插入mysql数据记录前，先要设置数据库字符集

```mysql
mysql> ALTER TABLE app01_book CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
Query OK, 0 rows affected (0.12 sec)
Records: 0  Duplicates: 0  Warnings: 0
```





方式一：实例化创建表的类

```python
from django.shortcuts import render,HttpResponse
from app01.models import Book

def index(request):
    book_obj=Book(id='1',title='python从入门到精通',state=True,pub_date='2012-12-10',price=120,publish='人民出版社')
    book_obj.save()
    return HttpResponse('OK')
```



方式二：

```python
from django.shortcuts import render,HttpResponse
from app01.models import Book

def index(request):
	#每张表下都有一个增删改查的objects的管理器,create返回值就是当前生成的对象记录
    book_obj = Book.objects.create(title='python从入门到精通',state=True,pub_date='2012-12-10',price=120,publish='人民出版社')
    #可以打印对象下的每一列的属性
    print(book_obj.title)
    print(book_obj.pub_date)
    return HttpResponse('OK')
```

