from django.shortcuts import render,HttpResponse,redirect
from app01.models import *
from django.core.paginator import Paginator,EmptyPage

def books(request):
    book_list=Book.objects.all().order_by('nid')

    paginator = Paginator(book_list,5)

    try:
        current_page_num = int(request.GET.get('page',1))
        current_page_obj = paginator.page(current_page_num)

        if current_page_num-5<=0:
            page_count=range(1,12)
        elif current_page_num+5>paginator.num_pages:
            page_count=range(paginator.num_pages-10,paginator.num_pages+1)
        else:
            page_count=range(current_page_num-5,current_page_num+6)

    except EmptyPage as e:
        print(e)
        current_page_obj = paginator.page(1)

    return render(request,'books.html',locals())

def addbook(request):
    if request.method == 'POST':
        print(request.POST)
        title=request.POST.get('title')
        price=request.POST.get('price')
        pubdate=request.POST.get('pubdate')
        publish=request.POST.get('publish')
        # 在HTML的select标签中选择了多个值，那么在request.POST中传递过来的是个列表
        author=request.POST.getlist('author')
        publish_obj=Publish.objects.get(name=publish)
        book_obj=Book.objects.filter(title=title).first()
        if book_obj:
            Book.objects.filter(title=title).update(title=title,price=price,pubdate=pubdate,publish=publish_obj)
        else:
            book_obj=Book.objects.create(title=title,price=price,pubdate=pubdate,publish=publish_obj)
        book_obj.authors.clear()
        for name in author:
            author_obj=Author.objects.filter(name=name).first()
            book_obj.authors.add(author_obj)
        return redirect('/books/')
    titles=Book.objects.values_list('title')
    author_objs=Author.objects.all()
    publish_names=Publish.objects.all().values('name')
    return render(request,'addbook.html',locals())

def delbook(request,nid):
    book_obj=Book.objects.filter(nid=nid).first()
    print(book_obj)
    book_obj.authors.clear()
    Book.objects.filter(nid=nid).first().delete()

    return redirect('/books')

def uptbook(request,nid):
    if request.method == 'POST':
        print('nonono',request.POST)
        title=request.POST.get('title')
        price=request.POST.get('price')
        pubdate=request.POST.get('pubdate')
        publish=request.POST.get('publish')
        publish_obj=Publish.objects.filter(name=publish).first()
        author_list=request.POST.getlist('author')
        book_obj=Book.objects.filter(title=title).first()
        if book_obj:
            Book.objects.filter(title=title).update(title=title, price=price, pubdate=pubdate, publish_id=publish_obj)
        else:
            book_obj=Book.objects.create(title=title, price=price, pubdate=pubdate, publish_id=publish_obj.nid)
        book_obj.authors.clear()
        for author in author_list:
            author_obj=Author.objects.filter(name=author).first()
            book_obj.authors.add(author_obj)
        return redirect('/books')
    book_obj=Book.objects.filter(nid=nid).first()
    nid = book_obj.nid
    title = book_obj.title
    price = book_obj.price
    pubdate = book_obj.pubdate
    publish_names=Publish.objects.all()
    publish_name = book_obj.publish
    author_names = Author.objects.all()
    book_author = book_obj.authors.all()
    print(author_names)
    return render(request,'addbook.html',locals())