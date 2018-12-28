django之choice方法



For every field that has [`choices`](https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.Field.choices) set, the object will have a `get_FOO_display()` method, where `FOO` is the name of the field. This method returns the “human-readable” value of the field.

For example:

```python
class UserInfo(AbstractUser):
    nid=models.AutoField(primary_key=True)
    # 使用choice功能选项，指定一个元祖，当数据库中存储的是18611223344，那么在HTML模板中调用{{ user.get_telephone_display }}后，将变为元祖中该手机号对应的信息
    phone_list = (
        ('18611223344', 'wangxin de phone'),
        ('13911223344', 'who de phone'),
    )
    telephone=models.CharField(max_length=11,null=True,unique=True,choices=phone_list)

```