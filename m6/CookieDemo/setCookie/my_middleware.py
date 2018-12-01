from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect
import time

view_count=1
start_time = ''
end_time = ''
host_info={}
host_list=[]

class IPViewCount(MiddlewareMixin):

    def process_request(self,request):
        global view_count

        for host in host_list:
            if request.get_host()==host:
                for i in host_info:
                    if time.time()-host_info[i][1]>10:
                        host_list.remove(i)
                        host_info.pop(i)
                        view_count=1
                        return redirect('/login/')
                    else:
                        return HttpResponse('连接次数过多，请%s秒后再试'
                                            %(10-int(time.time()-host_info[i][1])))

        start_time=time.time()

        view_count+=1
        host_name=request.get_host()
        if host_name not in host_info.keys():
            host_info[host_name]=[]
            host_info[host_name].append(view_count)
            host_info[host_name].append(start_time)
        else:
            host_info[host_name][0]+=1

    def process_response(self,request,response):

        end_time=time.time()

        for host_info_key,host_info_value in host_info.items():
            print(host_info_value)
            if host_info_value[0]>5:
                if end_time-host_info_value[1]<10:
                    if host_info_key not in host_list:
                        host_list.append(host_info_key)
                        host_info_value[1]=time.time()

        return response

