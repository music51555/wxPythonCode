from django.shortcuts import render,HttpResponse
from app1.models import Book
import datetime

old_book=None

def books(request):
    path = request.path_info
    if request.method == 'POST':
        book_title=request.POST.get('book_title')
        book_price=request.POST.get('book_price')
        book_pubdate=request.POST.get('book_pubdate')
        book_publish=request.POST.get('book_publish')

        if Book.objects.filter(title=book_title).exists():
            Book.objects.filter(title=book_title).update(price=book_price, pub_date=book_pubdate, publish=book_publish)
        else:
            print('old_book',old_book)
            if old_book:
                id = Book.objects.get(title=old_book).id
                Book.objects.filter(id=id).update(title=book_title, price=book_price, pub_date=book_pubdate,
                                                  publish=book_publish)
            else:
                Book.objects.create(title=book_title, price=book_price, pub_date=book_pubdate, publish=book_publish)

    if Book.objects.exists():
        books_num=Book.objects.all().count()
        print(books_num)
        books_list=Book.objects.all()
    return render(request,'books.html',locals())

def add_book(request):
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    global old_book
    old_book=None
    return render(request,'addbook.html',{'now':now})

def del_book(request):
    path = request.path_info

    title = path.rsplit('/', 1)[1]
    Book.objects.filter(title=title).delete()
    if Book.objects.exists():
        books_num=Book.objects.all().count()
        books_list=Book.objects.all()
    return render(request,'books.html',locals())

def update_book(request):
    path = request.path_info

    date_info = path.rsplit('/', 1)[1]
    global old_book
    old_book = date_info.split('_')[0]
    book_title = date_info.split('_')[0]
    book_price = date_info.split('_')[1]
    book_pubdate = date_info.split('_')[2]
    book_publish = date_info.split('_')[3]

    return render(request,'addbook.html',locals())

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