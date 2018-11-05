from django.shortcuts import render,HttpResponse
from app01.models import Book
from app01.models import Publish

def index(request):
    # book_obj=Book(id='1',title='python从入门到精通',pub_date='2014-12-5',state=True,public='人民出版社',price=82.10)
    # book_obj.save()
    # return HttpResponse('OK')

    # book_obj=Book.objects.create(title='Linux大师',pub_date='2012-9-10',state=True,public='人民出版社',price=96.10)
    # print(book_obj.title)
    # print(book_obj.pub_date)

    # 1、all方法，由类的objects管理器调用，得到的结果是python独有的queryset数据类型，存放的是一个个对象，类似列表，支持序列方法
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

    # 4、get()，对于查询结果有且只有一个的时候，查询才有意义
    book_obj=Book.objects.get(title='python从入门到精通')
    print(book_obj.title)

    # 5、exclude()，查询条件以外的数据，返回值是queryset
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

def filter_search(request):
    # __gt表示大于，__lt表示小于，也可以结合使用，查询区间范围之内的数据
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

    # 先查询出数据后，再删除，
    # 返回值是一个字典，存储删除的记录数和表名，调用者queryset，(1, {'app01.Book': 1})
    ret=Book.objects.filter(title='JAVA高级技术').delete()
    print(ret)

    # 查询出多条结果后，选出第一条后删除，调用者是models
    Book.objects.filter(price=100).delete()

    # 修改数据，调用者queryset
    ret = Book.objects.filter(title='Linux大师').update(title='Linux典范')
    print(ret)
    return HttpResponse('OK')

def add(request):
    # 在插入书籍信息前，首先插入一条出版社信息，因为书籍表中有出版社的外键列publish_id
    # Publish.objects.create(name='北京出版社',city='北京',email='23215412@qq.com')

    # 1、多表查询第一种插入数据方式：直接指定外键字段的值
    book_obj=Book.objects.create(title='水浒传',price=199,publishDate='2012-9-8',publish_id=1)
    print(book_obj.title)
    # 虽然没有为publish传入publish_obj，但是设置了publish_id=1，Django会为其解析为publish_id=1的publish_obj
    print(book_obj.publish)
    print(book_obj.publish.email)

    publish_obj=Publish.objects.get(name='北京出版社')
    # 2、第二种插入数据方式，将查询出的publish_obj对象，作为外键的值传入，但实际存储的是出版社的id
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