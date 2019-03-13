from rbac.models import *
from luffy_permission.settings import PERMISSION_SESSION_KEY

def init_permission(request, username):


    permission_query = Permission.objects.filter(role__userinfo__username=username).values('title','url','icon','menu__title','menu__icon').distinct()

    # permission_menu_info = {}
    permission_list = []

    # 循环一级菜单queryset集合
    # for menu in menu_queryset:
        # 如果在字典中没有获取到当前字典中的key值，那么就创建一个
        # if not permission_menu_info.get(menu['title']):
        #     permission_menu_info[menu['title']] = []
        # 循环二级菜单queryset集合
    for permission in permission_query:
        # 将所有的权限都添加到字典中，key为一级菜单的名称
        # permission_menu_info[menu['title']].append(permission)
        permission_list.append(permission)

    print('permission_menu_list',permission_list)
    # 最后形成了一个以一级菜单为key，关联二级菜单信息为value的字典，存储到session中
    request.session[PERMISSION_SESSION_KEY] = permission_list