from rbac.models import *
from luffy_permission.settings import PERMISSION_SESSION_KEY

def init_permission(request, username):

    url_queryset = UserInfo.objects.filter(
                    username=username,roles__permissions__isnull=False).values('roles__permissions__url').distinct()

    url_list = [ item[PERMISSION_SESSION_KEY] for item in url_queryset ]

    request.session[PERMISSION_SESSION_KEY] = url_list