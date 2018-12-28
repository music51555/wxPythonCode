Django之modles下的字段类型：

AutoField：根据ID自动递增

BigAutoField：从`1`递增到`9223372036854775807` 

BigIntegerField：数值范围`-9223372036854775808`到 `9223372036854775807` 

BooleanField：布尔值，default设置默认值

CharField：存储字符串，必要参数：max_length

TextField：存储大量文本

DateField：存储日期，auto_now，每次修改后都会更新时间戳，auto_now_add：首次创建自动添加当前时间

DateTimeField：存储日期和时间

DecimalField：浮点数

EmailField：邮箱

FileField：`models.FileField(upload_to='uploads/%Y/%m/%d/')`当包含时间格式时，自动变为`MEDIA_ROOT`目录下的的`media/home/media/photos/2007/01/15 `