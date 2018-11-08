基于join双下划线的连续跨表查询

```python
def query():
# 如果不适用跨表查询，语法复杂
ret=AuthorDetail.objects.filter(telephone='13809091122').first().author.book_set.all().first().publish.name
    print(ret)

    # 查询手机号以138开头的作者出版过的书籍和书籍的出版社名称
    # 基表定制为书籍表，但是书籍表和作者详情表没有关系，导致无法过滤出以138开头的手机号作者，所以利用跨表查询，虽然书籍表与作者详情表没有关联，但是书籍表与作者表有多对多的关系，关联字段是authors，所以正向查询book_obj.auhtors，author表与authordetail表是一对一的关系，按字段book_obj.auhtors__authordetail建立关联book_obj.auhtors__authordetail__telephone__startswith='138'筛选出手机号为138的作者，此时要查看的是这个作者出版的书籍名称和书籍的出版社名称，由于基表是book表，所以values('title')即可，而且书籍表和出版社表是一对多关系，再次使用双下划线跨表查询，'publishname'跨表查询出出版社的名称
    ret=Book.objects.filter(authors__authordetail__telephone__startswith='138').values('title','publish__name')
    print(ret)
    
    
    # 1、先判断两张表是否有关系
    # 2、如果有关系确定使用正向查询还是反向查询：正向查询用字段，反向查询用表名小写
    # 3、如果没有关系join有关系的表，如book表与authordetail表没有关系，那么就使用book表先join author表 ，再join authordetail表
    # 反向查询   
        ret=Author.objects.filter(authordetail__telephone__startswith='138').values('book__title','book__publish__name')
    print(ret)

    return HttpResponse('OK')
```

