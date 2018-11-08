ORM之一对一关系跨表查询

##### 一对一关系跨表正向查询和反向查询：都是按照表名

一对一关系跨表查询，如正向作者表跨表查询作者详情表，或反向作者详情表查询作者信息

使用对象.一对一表名`author.authordetail`或`authordetail.author`查询

```python
def query(request):
	# 一对一关系表正向查询：按字段，作者对象.authordetail
    author_obj=Author.objects.get(name='alex')
    print(author_obj.authordetail.telephone)

    # 一对一关系表反向查询：对象.一对一的表名。没有了_set，因为一对一的关系，返回的不是一个set集合，而是一个独立的对象
    alex=AuthorDetail.objects.get(telephone='13809091122')
    print(alex.author.name)

    return HttpResponse('OK')
```
