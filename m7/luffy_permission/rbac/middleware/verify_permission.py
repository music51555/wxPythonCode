from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from luffy_permission.settings import PERMISSION_LIST_SESSION_KEY,WHITE_LIST,MENU_DICT_SESSION_KEY
import re

class VerifyPermission(MiddlewareMixin):

    def process_request(self, request):
        # 通过字典的get(key)方法获取value不会报错，得到的是一个列表，里面存放着每一个权限的字典，如[{权限1},{权限2},{权限3}]
        permission_list = request.session.get(PERMISSION_LIST_SESSION_KEY)
        # sorted_dict表示在初始化权限时，整理后的字典，包含一级菜单字典和二级菜单字典
        sorted_dict = request.session.get(MENU_DICT_SESSION_KEY)

        # 循环白名单，如果匹配白名单中的路径成功，那么就在中间件中return，直接去执行视图函数
        for url in WHITE_LIST:
            url_ret = re.search(url, request.path_info)
            if not url_ret:
                continue
            else:
                return

        if sorted_dict:
            # 循环字典，循环的内容是字典一级菜单的title和对应的每一个一级菜单的字典
            for menu_title, menu_info in sorted_dict.items():
                # 循环综合字典的时候，循环所有权限列表
                for permission in permission_list:
                    # 直到在permission_list中找出当前访问路径的权限字典
                    if not re.match('^'+permission['url']+'$', request.path_info):
                        continue
                    # 找到了这条权限的字典，开始循环综合字典中的二级菜单的字典所在的列表permission_list
                    if menu_info.get('permission_list'):
                        for permission_dict in menu_info['permission_list']:
                            # 首先判断一下当前访问的这个权限字典中有无pid属性，如果没有按照数据库表示为二级菜单，如果有则表示为按钮
                            if permission['pid']:
                                # 得到当前权限字典的中的pid值，判断是否等于我正在循环的二级菜单列表中每个二级菜单字典的id，如果不等于就再次循环，直到找到当前权限的父级二级菜单字典
                                if not permission['pid'] == permission_dict['id']:
                                    continue
                                # 为这个按钮权限的父级二级菜单添加class属性，变为selected，让他在html中加载时，获得该属性，变为选中状态，并将这个二级字典的一级菜单字典的class属性变为show可见状态
                                permission_dict['class'] = 'selected'
                                menu_info['class'] = 'show'
                                break
                            # 如果点击的二级菜单，那么它是没有pid属性值的，为None
                            else:
                                # 这时判断访问的二级菜单的路径是否等于当前访问的路径，如果不等于则再次循环下一个二级菜单字典，直到找到当前访问的路径权限等于的那个二级菜单路径，为其添加上selected类，并且如果这个二级菜单的一级菜单的类不是show可见状态，那么为其设置为show，因为初始化权限时，每一个一级菜单的class都为hide，让其在加载首页时，默认只显示一级菜单
                                if permission_dict['url'] == request.path_info:
                                    permission_dict['class'] = 'selected'
                                    if not menu_info['class'] == 'show':
                                        menu_info['class'] = 'show'
                                    break


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
