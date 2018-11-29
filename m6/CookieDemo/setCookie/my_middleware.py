from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class MiddleWare_1(MiddlewareMixin):

    def process_request(self,request):
        print('MiddleWare_1 to request')

    def process_view(self,request, callback, callback_args, callback_kwargs):
        # callback(request)
        print('MiddleWare_1 to view')

    def process_exception(self,request,exception):

        print('MiddleWare_1 to exception')

    def process_response(self,request,response):
        print('MiddleWare_1 to response')

        return response

class MiddleWare_2(MiddlewareMixin):

    def process_request(self,request):
        print('MiddleWare_2 to request')

    def process_view(self,request, callback, callback_args, callback_kwargs):
        print('MiddleWare_2 to view')

    def process_exception(self, request, exception):
        print('MiddleWare_1 to exception')

    def process_response(self,request,response):
        print('MiddleWare_2 to response')

        return response