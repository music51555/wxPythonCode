ORM之删除和修改数据

查询出数据后再删除

查询出数据后再修改

```python
from django.shortcuts import render,HttpResponse
from app01.models import Book

def filter_search(request):
    # 先查询出数据后，再删除，
    # 返回值是一个字典，存储删除的记录数和表名，调用者queryset，(1, {'app01.Book': 1})
    ret=Book.objects.filter(title='JAVA高级技术').delete()
    print(ret)

    # 查询出多条结果后，选出第一条后删除，调用者是models
    Book.objects.filter(price=100).delete()

    # 修改数据，调用者queryset
    ret = Book.objects.filter(title='Linux大师').update(title='Linux典范')
    print(ret)
    return HttpResponse('OK')
```
