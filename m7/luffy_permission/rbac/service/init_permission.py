from rbac.models import *
from luffy_permission.settings import PERMISSION_LIST_SESSION_KEY,MENU_LIST_SESSION_KEY

def init_permission(request, username):

    menu_queryset = Menu.objects.values('title','icon')
    permission_query = Permission.objects.filter(role__userinfo__username=username).values('title','icon','url','menu__title','menu__icon')

    permission_list = []
    menu_list = []
    menu_dict = {}

    # 循环主菜单的过程中，循环子菜单，将所有的子菜单的信息添加到列表中，形成权限列表。[{权限1}，{权限2}]，用于在中间件verify_permission中循环，验证当前访问的路径，何其当前用户所有拥有权限的url是否匹配
    # 循环过程中，如果子菜单的父菜单标题和当前循环过程中的父菜单标题一致，那么就生成一个字典，变为{父菜单名称:[{子菜单1信息}，{子菜单2信息}]}
    # 最后变成[{父菜单1名称:[{子菜单1信息}，{子菜单2信息}]}，{父菜单2名称:[{子菜单1信息}，{子菜单2信息}]}]，用于在html网页中循环加载菜单使用
    for menu in menu_queryset:
        menu['class'] = 'hide'
        for permission in permission_query:
            permission_list.append(permission)
            if permission['menu__title'] == menu['title']:
                if not menu.get('permission_list'):
                    menu['permission_list'] = []
                menu['permission_list'].append(permission)

    print('menu',menu)
    print('permission_list',permission_list)
    # 以列表形式存储主菜单列表和子菜单列表，形成有序的列表，可以在加载菜单时，不会改变菜单的位置和顺序
    request.session[PERMISSION_LIST_SESSION_KEY] = permission_list
    request.session[MENU_LIST_SESSION_KEY] = menu_list