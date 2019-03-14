from django import template
from luffy_permission.settings import MENU_LIST_SESSION_KEY

register = template.Library()

@register.inclusion_tag('static_menu.html')
def static_menu(request):
    menu_list = request.session.get(MENU_LIST_SESSION_KEY)

    return {'menu_list': menu_list,'request':request}