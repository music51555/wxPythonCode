from django.shortcuts import render,HttpResponse
from app01.models import Book

def index(request):
    # book_obj=Book(id='1',title='python从入门到精通',state=True,pub_date='2012-12-10',price=120,publish='人民出版社')
    # book_obj.save()

    book_obj = Book.objects.create(title='python从入门到精通',state=True,pub_date='2012-12-10',price=120,publish='人民出版社')
    print(book_obj.title)
    print(book_obj.pub_date)
    return HttpResponse('OK')