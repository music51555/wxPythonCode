from django.shortcuts import render,HttpResponse
from app01.models import *

def books(request):
    ret=Book.objects.all().exists()
    return render(request,'books.html',locals())