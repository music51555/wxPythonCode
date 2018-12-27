session参数设置

将配置内容写在`settings.py`中

```python
SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周)
SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期
SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存,如设置session一周后失效，但是一周内再次登录，使得session的失效时间继续推迟一周，只要每次登录成功，就会保存session
```

