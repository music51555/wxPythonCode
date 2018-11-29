from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect
from CookieDemo import settings
from django.contrib import auth
import time

view_count=1
start_time = ''
end_time = ''
host_dict={}
host_timer={}
host_name_list=[]

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

class IPViewCount(MiddlewareMixin):

    def process_request(self,request):
        global start_time,view_count,host_timer,host_name_list,host_dict

        for host in host_name_list:
            if request.get_host()==host:
                for i in host_timer:
                    if time.time()-host_timer[host]>10:
                        host_name_list.remove(host)
                        host_dict.pop(host)
                        host_timer.pop(host)
                        print(host_name_list)
                        print(host_dict)
                        print(host_timer)
                        return redirect('/login/')
                    else:
                        print(time.time()-host_timer[host])
                return HttpResponse('连接次数过多，请10秒后再试')

        start_time=time.time()

        view_count+=1
        host_name=request.get_host()
        if host_name not in host_dict.keys():
            host_dict[host_name]=view_count
            host_timer[host_name]=start_time
        else:
            host_dict[host_name]+=1


    def process_response(self,request,response):
        global end_time,start_time,host_dict,host_name_list,host_timer

        end_time=time.time()

        for host_key_in_dict,counter in host_dict.items():
            if counter>2:
                for host_key_in_timer,timer in host_timer.items():
                    if end_time-timer<6:
                        if host_key_in_timer not in host_name_list:
                            host_name_list.append(host_key_in_timer)
                            host_timer[host_key_in_timer]=time.time()

        return response

