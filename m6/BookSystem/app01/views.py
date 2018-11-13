from django.shortcuts import render,HttpResponse,redirect
from app01.models import *

def books(request):
    num=1
    total_book=[]
    ret=Book.objects.all()
    for book_obj in ret:
        per_book = {}
        nid=book_obj.nid
        title=book_obj.title
        price=book_obj.price
        pubdate=book_obj.pubdate
        publish=book_obj.publish.name
        authors=book_obj.authors.all()
        per_book['nid']=nid
        per_book['num']=num
        per_book['title']=title
        per_book['price']=price
        per_book['pubdate']=pubdate
        per_book['publish']=publish
        per_book['authors']=authors
        total_book.append(per_book)
        num+=1
    print(total_book)
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
            author_obj=Author.objects.filter(name=name).first()
            book_obj.authors.add(author_obj)
        return redirect('/books/')
    titles=Book.objects.values_list('title')
    print(titles)
    author_objs=Author.objects.all()
    print(author_objs)
    publish_names=Publish.objects.all().values('name')
    return render(request,'addbook.html',locals())

def delbook(request,nid):
    book_obj=Book.objects.filter(nid=nid).first()
    print(book_obj)
    book_obj.authors.clear()
    Book.objects.filter(nid=nid).first().delete()

    return redirect('/books')