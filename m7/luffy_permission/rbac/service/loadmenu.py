from luffy_permission.settings import PERMISSION_SESSION_KEY
from web.models import *


def load_menu(request):
    customer_menu_info = request.session.get(PERMISSION_SESSION_KEY)
    menu_list = []

    for permission in customer_menu_info:
        if permission['is_menu'] == True:
            menu_list.append(permission)

    return menu_list

