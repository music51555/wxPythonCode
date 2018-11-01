from django.shortcuts import render,HttpResponse
from app1.models import Book

def books(request):
    if Book.objects.exists():
        books_num=Book.objects.all().count()
        print(books_num)
        books_list=Book.objects.all()
    return render(request,'books.html',locals())

def addbook(request):
    return render(request,'addbook.html')

def addbookinfo(request):
    if request.method == 'POST':
        book_title=request.POST.get('book_title')
        book_price=request.POST.get('book_price')
        book_pubdate=request.POST.get('book_pubdate')
        book_publish=request.POST.get('book_publish')
    Book.objects.create(title=book_title,price=book_price,pub_date=book_pubdate,publish=book_publish)
    return render(request,'books.html')
