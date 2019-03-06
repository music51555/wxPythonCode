from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
import re


class VerifyPermission(MiddlewareMixin):

    def process_request(self, request):
        if 'login' not in request.path_info and 'admin' not in request.path_info:
            if request.path_info not in request.session['user_permission_url']:
                return HttpResponse('没有权限访问')
