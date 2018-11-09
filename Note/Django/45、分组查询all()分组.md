分组查询扩展

group by主键、xxx1、xxx2和xxx3，与只group by 主键具有相同的意义，因为只有每一组的主键、xxx1、xxx2和xxx3相同时才会被分为一组

```python
#<QuerySet [{'name': '北京出版社', 'book__title__count': 5}]>，打印的结果是一个queryset类型，列表中的一个一个字典，实则还是一个一个对象，只是显示为字典形式，通过后面的values(xxx1,xxx2)，所指定显示的字段，实则还是这个对象（表）所拥有的字段，如Book.objects.values(xxx)......values(xxx1,xxx2)，其中xxx1和xxx2为Book表中的字段
ret=Book.objects.values('pk').annotate(max_author=Count('authors__nid')).values('title','max_author')
print(ret)

# 而使用all()进行分组，相当于是使用每一个字段进行分组，也就是开头说的只有每一组的主键、xxx1、xxx2和xxx3相同时才会被分为一组，这时的返回对象是[obj1,obj2,obj3]存储对象的queryset类型，在values中打印该对象表中的哪一列都是可以的，如打印了Book类表中的title和price，以及定义的max_author字段
ret=Book.objects.all().annotate(max_author=Count('authors__nid')).values('title','price','max_author')
print(ret)
```



#### 所以分组模型有2种：

```python
# 表模型.objects.values('pk').annotate(聚合函数(关联表的字段)).values('表模型的所有字段和统计字段')
Book.objects.values('pk').annotate(c_author=Count('authors__nid')).values('title','c_author')

# 加不加all()都表示查询出所有字段，而且all()分组与values('pk')分组是具有一样意义的，因为查询出所有的字段进行分组包含了主键，所以分组结果也是相同的，在Django官方文档中有使用这种分组
Book.objects.all().annotate(c_author=Count('authors__nid')).values('title','c_author')
Book.objects.annotate(c_author=Count('authors__nid')).values('title','c_author')
```

