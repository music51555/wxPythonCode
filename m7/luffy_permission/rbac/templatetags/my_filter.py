from django import template
from luffy_permission.settings import MENU_DICT_SESSION_KEY

register = template.Library()

@register.inclusion_tag('static_menu.html')
def static_menu(request):
    menu_dict = request.session.get(MENU_DICT_SESSION_KEY)

    return {'menu_dict': menu_dict,'request':request}