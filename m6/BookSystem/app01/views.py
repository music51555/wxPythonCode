from django.shortcuts import render,HttpResponse,redirect
from app01.models import *

def books(request):
    ret=Book.objects.values_list('title')
    print(ret)
    return render(request,'books.html',locals())

def addbook(request):
    if request.method == 'POST':
        print(request.POST)
        title=request.POST.get('title')
        price=request.POST.get('price')
        pubdate=request.POST.get('pubdate')
        publish=request.POST.get('publish')
        author=request.POST.getlist('author')
        publish_obj=Publish.objects.get(name=publish)
        book_obj=Book.objects.create(title=title,price=price,pubdate=pubdate,publish=publish_obj)
        for name in author:
            author_obj=author_obj=Author.objects.filter(name=name).first()
            book_obj.authors.add(author_obj)
        return redirect('/books/')
    author_objs=Author.objects.all()
    print(author_objs)
    publish_names=Publish.objects.all().values('name')
    return render(request,'addbook.html',locals())