
from django import template
import datetime

register=template.Library()

@register.filter
def my_datetime(my_time):
    my_time=datetime.datetime.strftime(my_time,'%Y-%m-%d %H:%M:%S')
    print(my_time   )
    return my_time