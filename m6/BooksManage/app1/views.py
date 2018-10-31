from django.shortcuts import render,HttpResponse
from app1.models import Book

def books(request):
    if Book.objects.exists():
        books_num=Book.objects.all().count()
        print(books_num)
        books_list=Book.objects.all()
    return render(request,'books.html',locals())