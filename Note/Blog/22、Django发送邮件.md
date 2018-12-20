`Django`发送邮件

首先需要在项目的`settings.py`中设置邮箱信息：

```python
EMAIL_HOST = 'smtp.qq.com'
EMAIL_POST = 465
# 发送者的邮箱，如果不写，将默认使用DEFAULT_FROM_EMAIL邮箱
EMAIL_HOST_USER = '452427904@qq.com'
# 在qq邮箱开启smtp服务后，开放了连接密码，使用此密码
EMAIL_HOST_PASSWORD = 'dqccbhjmkjxpbgig'
# DEFAULT_FROM_EMAIL = ''
EMAIL_USE_SSL = False
```



通过线程发送邮件，执行效率高，分别需要传入文章标题、文章内容、发送方邮箱，接收人邮箱参数

```python
from django.core.mail import send_mail

t = threading.Thread(target=send_mail, args=('您的%s文章收到一条新评论'%article_obj.title,
                                                  comment_content,
                                                  EMAIL_HOST_USER,
                                                  ['452427904@qq.com', ]
                                             ))
t.start()
```