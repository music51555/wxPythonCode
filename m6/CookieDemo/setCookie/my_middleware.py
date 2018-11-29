from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect
from CookieDemo import settings
from django.contrib import auth

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

class AuthMiddleWare(MiddlewareMixin):

    def process_request(self,request):
        white_list=settings.WHITE_LIST

        if request.path in white_list:
            # 如果在中间件中返回None，那么将结束中间件的执行过程
            return None

        # 只有在用户登录后，并且执行了auth.authenticate(username=xx,password=xx)后，request.user才是当前登录用户，否则为匿名用户。如果当前登录用户的not is_authenticated为True的话，那么就表示用户没有登录，那么将重定向到登录页面
        if not request.user.is_authenticated:
            return redirect('/login/')