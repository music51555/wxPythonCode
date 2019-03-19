from django import template
from luffy_permission.settings import MENU_DICT_SESSION_KEY,PERMISSION_LIST_SESSION_KEY

register = template.Library()

@register.inclusion_tag('static_menu.html')
def static_menu(request):
    menu_dict = request.session.get(MENU_DICT_SESSION_KEY)

    return {'menu_dict': menu_dict,'request':request}


@register.inclusion_tag('view_nav.html')
def view_nav(request):
    permission_list = request.session[PERMISSION_LIST_SESSION_KEY]

    for permission in permission_list:
        if permission['url'] == request.path_info:
            current_title = permission['title']
            current_url = permission['url']
            if permission['pid']:
                p_title = permission['pid__title']
                p_url = permission['pid__url']
                return {'p_title': p_title, 'p_url':p_url, 'current_title': current_title,'current_url':current_url}
            return {'current_title':current_title,'current_url':current_url}