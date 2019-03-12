from django import template
from luffy_permission.settings import PERMISSION_SESSION_KEY

register = template.Library()

@register.inclusion_tag('static_menu.html')
def static_menu(request):
    menu_info = request.session.get(PERMISSION_SESSION_KEY)

    return {'menu_info': menu_info,'request':request}