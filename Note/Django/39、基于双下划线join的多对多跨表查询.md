基于双下划线join的多对多跨表查询 

正向查询

反向查询

```python
def query:
	# 书籍表和作者表是多对多的关系，创建书籍表时有authors关联字段
    # 正向查询：按字段，SQL语句是书籍表join关系表book_author表，再join作者表查询出结果
    # <QuerySet [{'authors__name': 'alex'}, {'authors__name': 'egon'}]>
    ret=Book.objects.filter(title='西游记').values('authors__name')
    print(ret)
    # select t2.name from app01_book inner join app01_book_authors as t1
    # on app01_book.nid = t1.book_id
    # inner join app01_author as t2 on t1.author_id = t2.nid
    # where app01_book.title='西游记'

    # 反向查询按表名小写，作者表join关系表book_author，在join书籍表查询出结果
    # <QuerySet [{'name': 'alex'}, {'name': 'egon'}]>
    ret=Author.objects.filter(book__title='西游记').values('name')
    print(ret)
    # SELECT `app01_author`.`name` FROM `app01_author` INNER JOIN `app01_book_authors` ON 		(`app01_author`.`nid` = `app01_book_authors`.`author_id`) INNER JOIN `app01_book` ON 		(`app01_book_authors`.`book_id` = `app01_book`.`nid`) WHERE `app01_book`.`title` = '西游记' 

    return HttpResponse('OK')
```



