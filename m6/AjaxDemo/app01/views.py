from django.shortcuts import render,HttpResponse
from app01.models import *
from django.core.paginator import Paginator
import json

def upload(request):

    if request.method == 'POST':
        print(request.POST)
        file_obj=request.FILES.get('upload')
        with open(file_obj.name,'wb') as f:
            for line in file_obj:
                f.write(line)

    return render(request,'upload.html')

def index(request):
    # book_list=[]
    #
    # for i in range(100):
    #     book_obj=Book(title='book_%s'%i,price=i)
    #     book_list.append(book_obj)
    #
    # Book.objects.bulk_create(book_list)

    book_list=Book.objects.all()

    paginator=Paginator.



    return render(request,'book_list.html',locals())