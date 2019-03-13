from django import template
from luffy_permission.settings import PERMISSION_SESSION_KEY

register = template.Library()

@register.inclusion_tag('static_menu.html')
def static_menu(request):
    permission_list = request.session.get(PERMISSION_SESSION_KEY)

    return {'permission_list': permission_list,'request':request}