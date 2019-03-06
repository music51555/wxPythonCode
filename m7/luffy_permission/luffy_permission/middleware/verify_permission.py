from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
import re


class VerifyPermission(MiddlewareMixin):

    white_list = ['/register/','/login/']

    def process_request(self, request):
        print('111111111111')
        permission_list = request.session.get('user_permission_url')
        if not permission_list:
            if request.path_info not in self.white_list:
                return HttpResponse('请先登录')
        else:
            for url in permission_list:
                ret = re.search(url,request.path_info)

                print('222222222222222',request.path_infoc)
                if not ret:
                    return HttpResponse('没有权限访问')

