from django.shortcuts import render,HttpResponse
from app1.models import Book
import datetime

def books(request):
    path = request.path_info
    print(path)
    if 'del' in path:
        title=path.rsplit('/',1)[1]
        Book.objects.filter(title=title).delete()

    if request.method == 'POST':
        book_title=request.POST.get('book_title')
        book_price=request.POST.get('book_price')
        book_pubdate=request.POST.get('book_pubdate')
        book_publish=request.POST.get('book_publish')
        Book.objects.create(title=book_title,price=book_price,pub_date=book_pubdate,publish=book_publish)

    if Book.objects.exists():
        books_num=Book.objects.all().count()
        print(books_num)
        books_list=Book.objects.all()
    return render(request,'books.html',locals())

def addbook(request):
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    print(now)
    return render(request,'addbook.html',{'now':now})