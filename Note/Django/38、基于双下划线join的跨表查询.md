基于双下划线join的跨表查询

正向查询按字段

反向查询按表名

#### 一对多关系双下划线join跨表查询，类似于一对多关系的子查询跨表查询：

##### 1、join是先查找出书籍对象，通过书籍对象.values(外键列__属性)得到指定列值

##### 2、子查询是县查找出书籍对象，通过书籍对象.外键列.属性得到指定列值

```python
# 查询出出版过金瓶梅这个本书籍的出版社名称
def query(request):
	# 先按照书名查找出书籍对象，通过书籍对象.values(外键列)，相当于得到了外键列的出版社对象，并通过__出版社表的列名得到跨表查询的列值
    # 正向查询按字段
    ret=Book.objects.filter(title='金瓶梅').values('publish__name')
    # 打印<QuerySet [{'publish__name': '北京出版社'}]>
    print(ret)
    # 返回queryset类型，得到第一个字典对象后，通过get方法取值
    print(ret[0].get('publish__name'))
    
    
    # 一对多关系反向查询，通过出版社反向查询出：出版过金瓶梅这本书的出版社
    # 反向查询按表名
    ret=Publish.objects.filter(book__title='金瓶梅').values('name')
    print(ret)

    return HttpResponse('OK')
```



