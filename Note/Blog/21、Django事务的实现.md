`Django`事务的实现

**atomic**  /ə'tɑmɪk/  原子的，原子能的；微粒子的 

```python
from django.db import transaction

# 引入tranction事务后，调用with transaction.atomic():就可以实现事务，如其一一条代码失败，则整个事务提交失败
with transaction.atomic():
            comment_obj=Comment.objects.create(
                article_id=article_id, content=comment_content, user_id=request.user.pk, parent_comment_id=parent_pid)
            # xin
            Article.objects.filter(pk=article_id).update(comment_count=F('comment_count')+1)
```

