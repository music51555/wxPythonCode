#### 跨表查询的类型：

##### 1、join查询（双下划线查询）：

将多张表连接在一起合并为一张表查询



##### 2、子查询（基于对象的跨表查询）：

一个查询依赖于另一个查询结果之上



### 基于对象的跨表查询

**多对一**和**多对多**关系跨表正向查询：按字段，反向查询：表名_set.all()

#### 多对一关系跨表查询

```python
def query(request):
    # 跨表查询之正向查询：按字段查询
    # 一对多关系表中，在多的表中查询出外键publish字段的出版社对象，通过出版社对象查询出版社的其他信息
    book_obj=Book.objects.get(title='西游记')
    print(book_obj.publish.name)

    # 跨表查询之反向查询：表名_set.all()
    publish_obj=Publish.objects.get(name='北京出版社')
    # 出版社对象.book_set.all()，反向查询出与出版社对象关联的书籍对象，返回的是queryset类型
    print(publish_obj.book_set.all())

    return HttpResponse('OK')
```



转换为SQL语句是：

```mysql
# 先在book表中查询出title=西游记的这本书出版社的publish_id，然后在出版社表中查询id=xx的出版社名称
select name from publish where nid=(select publish_id from book where title = '西游记') 
```

