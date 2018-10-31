ORM查询表数据

`all()`、`first()`、`last()`、`get()`、`exclude`、`order_by`、`reverse()`、`count()`、`exists()`

`values`、`values_list`、`distinct()`

```python
from django.shortcuts import render,HttpResponse
from app01.models import Book

def index(request):
    # 1、all方法，由类的objects管理器调用，得到的结果是python独有的queryset数据类型，存放的是一个个对象，也就是表中的一条条记录，类似列表，支持序列方法
    book_list=Book.objects.all()
    print(book_list)

    # 类似列表，支持序列索引，得到的是这一条记录的对象，可以通过列名，查询出列值
    print(book_list[0].title)

    # 类似列表，支持for循环
    for i in book_list:
        print(i.title)

    # 2、first、last方法,返回值是book_obj对象
    book_obj1=Book.objects.all().first()
    # 等价于
    book_obj=Book.objects.all()[0]
    book_obj2=Book.objects.all().last()
    print(book_obj1.title)
    print(book_obj2.price)

    # 3、filter()，对应sql语句中的where，返回值是queryset类型
    book_list=Book.objects.filter(title='Linux大师')
    print(book_list[0].title)

    # 4、get()，对于查询结果有且只有一个的时候，查询才有意义，返回的是book_obj对象
    book_obj=Book.objects.get(title='python从入门到精通')
    print(book_obj.title)

    # 5、exclude()，美 /ɪk'sklʊd/ 排除，查询条件以外的数据，返回值是queryset
    book_list=Book.objects.exclude(title='python从入门到精通')
    print(book_list)

    # 6、order_by()，排序，"id"表示ASC升序，"-id"表示DESC降序，调用者queryset，返回的也是queryset
    book_list=Book.objects.all().order_by('-id')
    for i in book_list:
        print(i.id)

    # 7、reverse()，倒序输出结果，调用者queryset
    book_list=Book.objects.all().reverse()
    print(book_list)

    # 8、count()，统计查询结果的总数，调用者queryset
    num=Book.objects.all().count()
    print(num)

    # 9、exists()，判断查询结果是否为空，如果有数据则返回True，没有数据返回False
    b=Book.objects.filter(title='python从入门到精通').exists()
    print(b)

    # 10、values()，查询一列或多列的所有列值，返回结果是queryset类型，但存储的是字典形式，而不是obbk_obj形式，[{查询的列1:列值},{查询的列2:列值}]
    # 单条查询的结果<QuerySet [{'title': 'python从入门到精通'}, {'title': 'Linux大师'}]>
    # 多条查询的结果<QuerySet [{'title': 'python从入门到精通', 'price': Decimal('82.10')}, {'title': 'Linux大师', 'price': Decimal('96.10')}]>
    book_list=Book.objects.all().values('title','price')
    print(book_list)

    # 11、values_list(),也是查询一列或多列的值，返回结果也是queryset类型，但存储的是元祖类型，在元祖中存储列值，[(列值1，列值2),(列值1，列值2)]
    # 查询结果<QuerySet [('python从入门到精通', Decimal('82.10')), ('Linux大师', Decimal('96.10'))]>
    book_list=Book.objects.all().values_list('title','price')
    print(book_list)

    # 12、distinct()、去重查询，返回结果是queryset类型
    # Book.objects.all().distinct()这样的去重查询没有意义，因为主键的关系，整张表中一定没有重复数据，要想去重查询，是针对单一列进行去重查询的
    # 搭配values()和values_list()使用，去除某一列的的重复结果，<QuerySet [{'price': Decimal('100.00')}, {'price': Decimal('150.00')}]>
    book_list=Book.objects.all().values('price').distinct()
    print(book_list)
    return HttpResponse('OK')
```



#### queryset类型支持链式查询

```python
Book.objects.all().filter().order_by().first()
```

