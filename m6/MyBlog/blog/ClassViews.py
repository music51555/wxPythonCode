from django.views import View
from django.shortcuts import HttpResponse

class my_views(View):

    def get(self,request):

        return HttpResponse('Hello world')