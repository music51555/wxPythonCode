from rbac.models import *
from luffy_permission.settings import PERMISSION_LIST_SESSION_KEY,MENU_DICT_SESSION_KEY

def init_permission(request, username):

    menu_queryset = Menu.objects.values('title','icon')
    permission_query = Permission.objects.filter(role__userinfo__username=username).values('title','icon','url','menu__title','menu__icon')

    permission_list = []
    menu_list = []
    menu_dict = {}

    # 登录后要初始化菜单权限，循环一级菜单时为每一个一级菜单添加class属性，其值为hide，表示默认每个要动态加载一级菜单的子菜单
    # 都会被添加hide类，让其子菜单隐藏起来，如果当前访问的路径和子菜单的路径一致，那么就把其子菜单的父菜单的hide类去除，让其子菜单正常显示
    for menu in menu_queryset:
        menu['class'] = 'hide'
        for permission in permission_query:
            # 把所有的子菜单都放在列表中，用于在中间件中验证用户有当前路径的访问权限
            permission_list.append(permission)
            if permission['menu__title'] == menu['title']:
                if not menu.get('permission_list'):
                    menu['permission_list'] = []
                menu['permission_list'].append(permission)
        menu_dict[menu['title']] = menu

    sorted_dict = {}
    # 由于字典时无序的，动态加载菜单时顺序可能会错乱，所以对字典排序，得到的结果是字典key排序的列表
    soreted_keys_list = sorted(menu_dict)

    # 循环列表，按排序后的key重新赋值value
    for menu_dict_key in soreted_keys_list:
        sorted_dict[menu_dict_key] = menu_dict[menu_dict_key]

    # 以列表形式存储主菜单列表和子菜单列表，形成有序的列表，可以在加载菜单时，不会改变菜单的位置和顺序
    request.session[PERMISSION_LIST_SESSION_KEY] = permission_list
    request.session[MENU_DICT_SESSION_KEY] = sorted_dict