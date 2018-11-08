基于双下划线join的一对多跨表查询

正向查询**按字段**

反向查询**按表名**

##### 

##### 正向查询：`Book.objects.filter(xxx).values('外键列_ _列名')`

##### 反向查询：`Publish.objects.filter(反向表名_ _列名).values(publish表列名)`

```python
# 查询出出版过金瓶梅这个本书籍的出版社名称

def query(request):
	# 先按照书名查找出书籍对象，通过书籍对象.values(外键列)，相当于得到了外键列的出版社对象，并通过__出版社表的列名得到跨表查询的列值
    
    # 正向查询按字段
    # SELECT publis.name FROM app01_book INNER JOIN app01_publish ON app01_book.publish_id = app01_publish.nid WHERE app01_book.title = '金瓶梅'
    ret=Book.objects.filter(title='金瓶梅').values('publish__name')
    # 打印<QuerySet [{'publish__name': '北京出版社'}]>
    print(ret)
    # 返回queryset类型，得到第一个字典对象后，通过get方法取值
    print(ret[0].get('publish__name'))
    
    
    # 一对多关系反向查询，通过出版社反向查询出：出版过金瓶梅这本书的出版社
    # 反向查询按表名
    # SELECT app01_publish.name FROM app01_publish INNER JOIN app01_book ON app01_publish`.`nid` = app01_book.publish_id WHERE app01_book.title = '金瓶梅'
    ret=Publish.objects.filter(book__title='金瓶梅').values('name')
    print(ret)

    return HttpResponse('OK')
```



