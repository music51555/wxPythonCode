from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect
# from CookieDemo import settings
from django.contrib import auth
import time
from collections import defaultdict


def _get_time():
    return time.time()


host_info = defaultdict(list)
view_count = 1


class IPViewCount(MiddlewareMixin):

    def process_request(self, request):
        self.start_time = _get_time()
        global view_count

        self.host_name = host_name = self._get_host(request)

        if host_name not in host_info.keys():
            host_info[host_name].extend([view_count, self.start_time])
        else:
            host_info[host_name][0] += 1

        self.lock_status = True if len(host_info.get(host_name)) > 2 else False

        if self.lock_status:
            return HttpResponse('连接次数过多，请%s秒后再试'%(10 - int(host_info.get(host_name)[3])))

    def process_response(self, request, response):
        end_time = _get_time()
        current_host_info = host_info.get(self.host_name)

        if current_host_info[0] >= 5:
            if end_time - current_host_info[1] < 10:
                if not self.lock_status:
                    current_host_info.extend(["locked", end_time - current_host_info[1]])
                else:
                    current_host_info[3] = end_time - current_host_info[1]
            else:
                host_info[self.host_name] = [1, end_time]

        return response

    def _get_host(self, request):
        return request.get_host()

c = IPViewCount()
print(c.host_name)