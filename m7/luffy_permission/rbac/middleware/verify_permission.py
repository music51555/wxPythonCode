from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from luffy_permission.settings import PERMISSION_SESSION_KEY,WHITE_LIST
import re

class VerifyPermission(MiddlewareMixin):

    def process_request(self, request):
        permission_list = request.session.get(PERMISSION_SESSION_KEY)

        if permission_list:
            for url in permission_list:
                print('path_info',request.path_info)
                per_ret = re.search(url, request.path_info)
                if not per_ret:
                    return HttpResponse('没有权限访问')
        else:
            if request.user.is_authenticated:
                return
            for url in WHITE_LIST:
                url_ret = re.search(url, request.path_info)
                if not url_ret:
                    continue
                else:
                    return
            return HttpResponse('请先登录')







