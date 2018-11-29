process_exception

**如果视图函数报错**，那么将会倒序执行所有中间件的`process_exception`方法，如果在某一个process_exception方法中有返回值`return`，那么将不会继续执行其他中间件中的`process_exception`方法

**如果视图函数没有报错，**那么不会执行中间件中的`process_exception`方法

```python
class MiddleWare_1(MiddlewareMixin):

    def process_request(self,request):
        print('MiddleWare_1 to request')

    def process_view(self,request, callback, callback_args, callback_kwargs):
        # callback(request)
        print('MiddleWare_1 to view')

    # 正常执行程序，不会输出process_exception方法中的内容，只有在视图函数报错时，才会输出
    def process_exception(self,request,exception):

        print('MiddleWare_1 to exception')

    def process_response(self,request,response):
        print('MiddleWare_1 to response')

        return response
```

![exception](.\images\exception.png)