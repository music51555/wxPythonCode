#### 多对多关系跨表查询

```python
def query(request):
    # 跨表查询之正向查询：按字段查询
    # 书籍与作者是多对多关系，是通过书籍表models.ManyToManyField()创建的第三张表，所以通过书籍查询作者是正向查询
    book_obj=Book.objects.get(title='西游记')
    # 查询出西游记这本书的全部作者，然后进行for循环遍历每一个作者，打印alex,egon
    author_list=book_obj.authors.all()
    for author in author_list:
        print(author.name)

    # 跨表查询之反向查询：表名_set.all()
    author_obj=Author.objects.get(name='alex')
    book_list=author_obj.book_set.all()
    # 打印西游记
    for book in book_list:
        print(book.title)

    return HttpResponse('OK')
```