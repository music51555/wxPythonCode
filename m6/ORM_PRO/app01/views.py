from django.shortcuts import render,HttpResponse
from app01.models import Book

def index(request):
    # book_obj=Book(id='1',title='python从入门到精通',pub_date='2014-12-5',state=True,public='人民出版社',price=82.10)
    # book_obj.save()
    # return HttpResponse('OK')

    book_obj=Book.objects.create(title='Linux大师',pub_date='2012-9-10',state=True,public='人民出版社',price=96.10)
    print(book_obj.title)
    print(book_obj.pub_date)
    return HttpResponse('OK')