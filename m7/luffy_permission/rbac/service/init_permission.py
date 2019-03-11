from rbac.models import *
from luffy_permission.settings import PERMISSION_SESSION_KEY

def init_permission(request, username):

    # url_queryset = UserInfo.objects.filter(
    #                 username=username,roles__permissions__isnull=False
    # ).values('roles__permissions__title','roles__permissions__url','roles__permissions__is_menu').distinct()

    menu_info = Menu.objects.filter(permission__role__userinfo__username = username).values('title','permission__title')
    print('menu_info',menu_info)

    menu_info = Menu.objects.values('title').values('title','permission__menu')
    print('menu_info',menu_info)


    # permission_info_list = []
    #
    # for item in url_queryset:
    #     permission_dict = {}
    #
    #     permission_dict['url'] = item['roles__permissions__url']
    #     permission_dict['title'] = item['roles__permissions__title']
    #     permission_dict['is_menu'] = item['roles__permissions__is_menu']
    #
    #     permission_info_list.append(permission_dict)
    #
    # request.session[PERMISSION_SESSION_KEY] = permission_info_list