from django import template
from luffy_permission.settings import PERMISSION_SESSION_KEY

register = template.Library()

@register.inclusion_tag('static_menu.html')
def static_menu(request):
    customer_menu_info = request.session.get(PERMISSION_SESSION_KEY)
    menu_list = []

    for permission in customer_menu_info:
        if permission['is_menu'] == True:
            menu_list.append(permission)

    return {'menu_list': menu_list,'request':request}