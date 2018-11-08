基于双下划线join一对一关系跨表查询

正向查询：按外键字段

```
Author.objects.filter(xxx).values(外键字段__列名)
```



反向查询：按表名小写

```
AuthorDetail.objects.filter(表名小写__列名).values(要查询的列)
```



```python
def query():
	# 一对一关系基于join双下划线跨表正向查询：按外键字段
    # <QuerySet [{'authordetail__telephone': '13809091122'}]>
    ret=Author.objects.filter(name='alex').values('authordetail__telephone')
    print(ret)

    # 一对一关系基于join双下划线跨表正向查询：按外键字段
    # <QuerySet [{'telephone': '13809091122'}]>
    ret=AuthorDetail.objects.filter(author__name='alex').values('telephone')
    print(ret)

    return HttpResponse('OK')
```

