from django.shortcuts import render,HttpResponse,redirect
from app1.models import Book
import datetime

old_book=None

def books(request):

    if Book.objects.exists():
        books_num=Book.objects.all().count()
        print(books_num)
        books_list=Book.objects.all()
    return render(request,'books.html',locals())

def add_book(request):
    if request.method=='POST':
        title = request.POST.get('book_title')
        price = request.POST.get('book_price')
        pub_date = request.POST.get('book_pubdate')
        publish = request.POST.get('book_publish')
        Book.objects.create(title=title,price=price,pub_date=pub_date,publish=publish)

        return redirect('/books/')

    now = datetime.datetime.now().strftime('%Y-%m-%d')

    return render(request,'addbook.html',{'now':now})

def del_book(request,id):
    Book.objects.filter(id=id).delete()

    return redirect('/books/')

def update_book(request,id):
    if request.method=='POST':
        title=request.POST.get('book_title')
        price=request.POST.get('book_price')
        pub_date=request.POST.get('book_pubdate')
        publish=request.POST.get('book_publish')
        Book.objects.filter(id=id).update(title=title,price=price,pub_date=pub_date,publish=publish)

        return redirect('/books/')

    book_obj=Book.objects.get(id=id)
    print('booj_obj',book_obj)

    return render(request,'addbook.html',{'book_obj':book_obj})

def search(request):
    book_list=Book.objects.filter(publish='老男孩出版社',price__gt=200)
    print(book_list)
    book_list=Book.objects.filter(pub_date__startswith='2017-08')
    print(book_list)
    book_list = Book.objects.filter(price__in=[50,100,150])
    print(book_list)
    book_list = Book.objects.filter(price__gt=100,price__lt=200)
    print(book_list)
    book_list = Book.objects.filter(publish='老男孩出版社').values('price').order_by('-price').distinct()
    print(book_list)
    return HttpResponse('OK')