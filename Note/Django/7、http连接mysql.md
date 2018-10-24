http连接mysql

```python
def auth(environ):
    # 在请求报文中查看‘REQUEST_METHOD’字典的值，查看HTTP的请求方式
    if environ.get("REQUEST_METHOD") == "POST":

        try:
            # 获取POST请求发送数据的长度，如'CONTENT_LENGTH': '24'
            request_body_size = int(environ.get('CONTENT_LENGTH'))
        except (ValueError):
            request_body_size = 0

        # 根据数据内容长度读取参数内容，并通过parse_qs获取数据
        request_body = environ['wsgi.input'].read(request_body_size)
        data = parse_qs(request_body)

        # 在data的字典中通过form表单的name值获取用户的输入值
        user = data.get(b"username")[0].decode("utf8")
        pwd = data.get(b"pwd")[0].decode("utf8")

        # 连接数据库，验证用户名和密码是否正确，正确与否返回不同的页面
        conn = pymysql.connect(
            host = '140.143.132.118',
            port = 3306,
            user = 'xiaoxin',
            password = 'Nishi458_2',
            db = 'm6',
            charset = 'utf8'
        )

        cursor = conn.cursor()
        sql = 'select * from userinfo where name = %s and pwd = %s'

        row = cursor.execute(sql,(user,pwd))
        if row:
            return b'<h1>welcome</h1>'
        else:
            return b'404'
```

