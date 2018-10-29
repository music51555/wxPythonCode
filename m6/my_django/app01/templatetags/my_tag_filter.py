from django import template

register=template.Library()

#过滤器是以“|”分隔的，如{{ i|multi_filter:10 }}，所以自定义过滤器时只能传入2个参数，i和10
@register.filter
def multi_filter(x,y):
    return x*y

#自定义标签可以传入多个参数，因为标签调用参数时，是以空格分隔的
@register.simple_tag
def multi_tag(x,y):
    return x*y