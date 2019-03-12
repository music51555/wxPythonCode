from rbac.models import *
from luffy_permission.settings import PERMISSION_SESSION_KEY

def init_permission(request, username):

    # 查询出所有的一级菜单
    menu_queryset = Menu.objects.all().values('title')

    permission_query = Permission.objects.filter(role__userinfo__username=username,menu__isnull=False).values('title','url','icon','menu__title','menu__icon')

    permission_menu_info = {}

    # 循环一级菜单queryset集合
    for menu in menu_queryset:
        # 如果在字典中没有获取到当前字典中的key值，那么就创建一个
        if not permission_menu_info.get(menu['title']):
            permission_menu_info[menu['title']] = []
        # 循环二级菜单queryset集合
        for permission in permission_query:
            # 判断如果二级菜单的父级菜单名称和循环中一级菜单的名称相匹配就在permission_menu_info字典中
            # 以父级菜单的名称为key，以二级菜单的信息为value形成一个字典
            if permission['menu__title'] == menu['title']:
                permission_menu_info[menu['title']].append(permission)

    # 最后形成了一个以一级菜单为key，关联二级菜单信息为value的字典，存储到session中
    request.session[PERMISSION_SESSION_KEY] = permission_menu_info