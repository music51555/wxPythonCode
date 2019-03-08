from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from luffy_permission.settings import PERMISSION_SESSION_KEY,WHITE_LIST
import re

class VerifyPermission(MiddlewareMixin):

    def process_request(self, request):
        # 通过字典的get(key)方法获取value不会报错
        permission_list = request.session.get(PERMISSION_SESSION_KEY)

        # 循环白名单，如果匹配白名单中的路径成功，那么就在中间件中return，直接去执行视图函数
        for url in WHITE_LIST:
            url_ret = re.search(url, request.path_info)
            if not url_ret:
                continue
            else:
                return

        # 循环session中的权限列表，如果匹配成功那么就让用户访问对应页面，如果没有匹配上就继续循环，最终没有匹配上则返回响应体没有权限访问
        if permission_list:
            for permission in permission_list:
                per_ret = re.match('^'+permission['url']+'$', request.path_info)
                if not per_ret:
                    continue
                else:
                    return
            return HttpResponse('没有权限访问')
        else:
            # 如果登录的用户有角色，但是角色内没有分配权限，所以permission_list就会为空，没有访问任何页面的权限
            if request.user.is_authenticated:
                return HttpResponse('没有权限访问')

            # 如果用户访问的不是白名单的路径，访问的是需要权限的路径，让其先登录
            return HttpResponse('请先登录')







