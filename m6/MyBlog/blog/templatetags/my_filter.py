
from django import template
from blog import models
from django.db.models import Count
from django.db.models.functions import TruncMonth


register = template.Library()

@register.inclusion_tag('cate_style.html')
def get_classification(username):
    print(username)
    user = models.UserInfo.objects.filter(username=username).first()
    blog = user.blog

    cate_list = models.Category.objects.values('nid').filter(blog=blog).annotate(
        article_count=Count('article__nid')).values('title', 'article_count')

    tag_list = models.Tag.objects.filter(blog=blog).values('nid').annotate(article_count=Count('article__nid')).values(
        'title', 'article_count')

    date_list = models.Article.objects.filter(user=user).annotate(month=TruncMonth('create_time')).values('month').annotate(
        article_count=Count('nid')).values('month', 'article_count')

    return {'cate_list': cate_list, 'tag_list': tag_list, 'date_list_2': date_list, 'username': username}


@register.filter
def to_replace(comment):
    if '@' in comment:
        comment = comment.replace('@', '<a href>@</a>')
        print(comment)

    return comment