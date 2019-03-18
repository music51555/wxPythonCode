from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from luffy_permission.settings import PERMISSION_LIST_SESSION_KEY,WHITE_LIST,MENU_DICT_SESSION_KEY
import re

class VerifyPermission(MiddlewareMixin):

    def process_request(self, request):
        # 通过字典的get(key)方法获取value不会报错，得到的是一个列表，里面存放着每一个权限的字典，如[{权限1},{权限2},{权限3}]
        permission_list = request.session.get(PERMISSION_LIST_SESSION_KEY)
        sorted_dict = request.session.get(MENU_DICT_SESSION_KEY)

        # 循环白名单，如果匹配白名单中的路径成功，那么就在中间件中return，直接去执行视图函数
        for url in WHITE_LIST:
            url_ret = re.search(url, request.path_info)
            if not url_ret:
                continue
            else:
                return

        parent_node = None

        if sorted_dict:
            for menu_title, menu_info in sorted_dict.items():
                for permission in permission_list:
                    if not request.path_info == permission['url']:
                        continue
                    # 此时在权限列表中找到了访问的路径的那一条数据，这时候开始循环菜单，验证那一条数据的pid是否等于
                    # 循环中的菜单的id，
                    for permission_dict in menu_info['permission_list']:
                        if permission['pid']:
                            if not permission['pid'] == permission_dict['id']:
                                continue
                            permission_dict['class'] = 'selected'
                        else:
                            if permission_dict['url'] == request.path_info:
                                permission_dict['class'] = 'selected'



        # 循环权限列表，用每一个权限字典中的url和当前请求的路径相匹配，判断其是否可以访问
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
