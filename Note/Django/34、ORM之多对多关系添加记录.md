ORM之多对多关系添加记录

如果按照单表插入数据的逻辑，应该是

```python
# 插入id为1的书籍，插入id为2的作者，到多对多的第三张关系表book2author中
book2author.objects.create(book_id=1,author_id=2)
```



但是，在`models.py`文件中并没有创建`book2author`类去创建表，而是通过如下创建的，所就不能使用`objects.create`这种方法

```python
authors=models.ManyToManyField(to='Author')
```



Django提供了API接口

```python
def addmany(request):
    book_obj=Book.objects.create(title="金瓶梅",price=198,publishDate="2012-9-8",publish_id=1)

    alex=Author.objects.get(name='alex')
    egon=Author.objects.get(name='egon')

    # 1、add方法，添加绑定关系
    # book_obj表示金瓶梅这本书，add的API接口表示为这本书籍在关系表中关联查询出来的作者对象alex，egon
    book_obj.authors.add(alex,egon)
    # 表示为金瓶梅这本书在关系表中添加作者表中nid为1和2的作者
    book_obj.authors.add(1,2)
    # 传入非固定参数也是一样的效果
    book_obj.authors.add(*[1,2])

    # 2、remove方法，解除绑定关系，查询出书籍对象，通过remove的API解除绑定关系
    book_obj=Book.objects.get(title='西游记')

    # 同样也是可以通过作者对象、作者id和非固定参数解除绑定
    book_obj.authors.remove(alex,egon)
    book_obj.authors.remove(1,2)
    book_obj.authors.remove(*[1,2])

    # 3、clear()方法，在关系表中清除所有与这本书关联的作者数据
    book_obj.authors.clear()

    # 4、all()方法，在关系表中查询出所有与这本书关联的作者对象，返回是queryset类型的列表
    print(book_obj.authors.all())

    # 5、支持queryset类型的values()方法，queryset类型的values方法：<QuerySet [{'name': 'alex'}, {'name': 'egon'}]>
    print(book_obj.authors.all().values("name"))

    return HttpResponse('OK')
```