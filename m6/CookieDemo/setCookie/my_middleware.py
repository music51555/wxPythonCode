from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect
from CookieDemo import settings
from django.contrib import auth
import time

view_count=1
start_time = ''
end_time = ''
host_info={}
host_timer={}
host_list=[]

class IPViewCount(MiddlewareMixin):

    def process_request(self,request):
        global view_count

        for host in host_list:
            if request.get_host()==host:
                for i in host_timer:
                    if time.time()-host_timer[host]>10:
                        host_list.remove(i)
                        host_info.pop(i)
                        host_timer.pop(i)
                        view_count=1
                        return redirect('/login/')
                    else:
                        return HttpResponse('连接次数过多，请%s秒后再试'%(10-int(time.time()-host_timer[host])))

        start_time=time.time()

        view_count+=1
        host_name=request.get_host()
        if host_name not in host_info.keys():
            host_info[host_name]=view_count
            host_timer[host_name]=start_time
        else:
            host_info[host_name]+=1

    def process_response(self,request,response):
        end_time=time.time()

        for host_info_key,counter in host_info.items():
            print('host_info_2', host_info)
            if counter>5:
                for host_timer_key,timer in host_timer.items():
                    if end_time-timer<10:
                        if host_timer_key not in host_list:
                            host_list.append(host_timer_key)
                            host_timer[host_timer_key]=time.time()

        return response

