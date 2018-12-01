`socketserver`是如何实现的

先看一下我们编写的代码：

```python
import socketserver

#继承于BaseRequestHandler类 /'hændlɚ/ 处理
class MyServer(socketserver.BaseRequestHandler):

    #重写父类的handle方法，因为handle是BaseRequestHandler父类中用于处理请求客户端请求的，所以重写handle方法，编写并发的处理逻辑
    def handle(self):
        print('new conn:',self.client_address)
        while True:
            try:
                # self.request表示接收的客户端套接字对象conn
                data = self.request.recv(1024)
                # ('127.0.0.1', 57195)可以通过索引打印IP和端口
                print('new conn',self.client_address[0])
                self.request.send(data.upper())
            except ConnectionResetError:
                break
            self.request.close()

if __name__ == '__main__':
    # ThreadingTCPServer传入ip和端口，以及自定义的socket类
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8087),MyServer)
    server.serve_forever()
```



**socketserver使用模式：**

1、自定义`socket`类

```python
class MyServer(socketserver,BaseRequestHandle):
	def handle():
		# 在里面填写socket服务端的代码
```



2、调用`socketserver`对象

```python
# ThreadingTCPServer表示利用多线程方式实现并发
server = socketserver.ThreadingTCPServer(('127.0.0.1',8087),MyServer)
```



3、启动`socketserver`服务

```
server.serve_forever()
```



**源代码分析：**

**提问：**为什么执行`server.serve_forever()`后，会执行自定义类中的`handler()`函数？

从运行的第一行代码开始分析

```python
server = socketserver.ThreadingTCPServer(('127.0.0.1',8086),Server)
```

`server`是通过`socketserver.ThreadingTCPServer`类的实例化得到的对象，**那么`server`是什么呢？**

`ThreadingTCPServer`的源码显示为，发现没有`__init__`方法，所以就无法实例化对象

```python
class ThreadingTCPServer(ThreadingMixIn, TCPServer): pass
```

`ThreadingTCPServer`类继承于`ThreadingMixIn`类和`TCPServer`类，所有从左至右依次查找

`ThreadingMixIn`类显示为，也没有找到`__init__`方法

```python
class ThreadingMixIn:
    daemon_threads = False

    def process_request_thread(self, request, client_address):
    	pass

    def process_request(self, request, client_address):
    	pass
```



继续查看`TCPServer`类，在该类下顺利的找到了`__init__`方法，检查与我们传入的参数相符，包含`server_address`和`RequestHandlerClass`，分别表示**连接地址`('127.0.0.1',8087)**`   和自定义的功能类``MyServer`

```python
class TCPServer(BaseServer):
	def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
        #调用了父类BaseServer的__init__方法
        BaseServer.__init__(self, server_address, RequestHandlerClass)

```



其中又发现了` BaseServer.__init__(self, server_address, RequestHandlerClass)`，调用了父类的实例化`__init__`方法，父类的`__init__`方法又做了什么事情呢？

```python
    def __init__(self, server_address, RequestHandlerClass):
        """Constructor.  May be extended, do not override."""
        # 进行了实例化变量赋值的操作，将传入IP和端口赋值为server_address变量
        # 将自定义的功能类赋值为RequestHandlerClass变量
        self.server_address = server_address
        self.RequestHandlerClass = RequestHandlerClass
        self.__is_shut_down = threading.Event()
        self.__shutdown_request = False
```



继续又创建了套接字对象socket

```python
 def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
      
        #address_family = socket.AF_INET
        #socket_type = socket.SOCK_STREAM
        #实例化socket对象
        self.socket = socket.socket(self.address_family,self.socket_type)
        if bind_and_activate:
            try:
                #建立服务端链接:
                #server_bind执行的是socket.setsockopt、socket.bind、以及通过socket.getsockname()得到服务端的IP地址
                #server_activate的方法是设置server.listen()
                self.server_bind()
                self.server_activate()
            except:
                self.server_close()
                raise
```



继续又执行了server_bind()方法，为服务端建立连接绑定IP和端口

```python
 def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
        if bind_and_activate:
            try:
                # 执行的是self.socket.bind(self.server_address)，绑定IP和端口
                self.server_bind()
                # 执行的是self.socket.listen(self.request_queue_size)，创建等待队列数
                self.server_activate()
            except:
                self.server_close()
                raise
```



所以现在看来，`server`对象就是通过`TCPServer`类实例化得到的对象，其中做了：

`1、实例化socket对象`

`2、绑定server.bind()`

`3、设置了server.listen(5)`



继续下一行代码

```python
server.serve_forever()
```



首先`serve_forever`是在`BaseServer`类下，也就是`TCPServer`类的父类



这句代码的含义是接收客户端连接

```python
    def serve_forever(self, poll_interval=0.5):
        self.__is_shut_down.clear()
        try:
            with _ServerSelector() as selector:
                
                selector.register(self, selectors.EVENT_READ)

                while not self.__shutdown_request:
               		#这一句就是我们所学过的多路复用，每隔poll_interval设置的0.5秒后，对比与阻塞IO的由server应用程序去询问操作系统是否获取到了客户端数据，变为由select这个中介每隔xx秒后去询问操作系统
                    ready = selector.select(poll_interval)
                    #如果有客户端连接，就调用_handle_request_noblock()方法
                    if ready:
                        self._handle_request_noblock()

                    self.service_actions()
        finally:
            self.__shutdown_request = False
            self.__is_shut_down.set()
```



在`BaseServer`下查看`_handle_request_noblock`函数：

```python
class BaseServer:
	def _handle_request_noblock(self):
        try:
            #表示通过get_request方法获取客户端的conn连接（这里用request表示）和连接地址。self.get_request()，self表示哪个对象？向上查找到当前函数_handle_request_noblock，再继续向上查找，又查找到了serve_forever()函数下的self._handle_request_noblock()，又是谁调用了serve_forever()，是通过ThreadingTCPServer类，继承的TCPServer下的get_request方法，其中return了 self.socket.accept()方法，等待客户端连接
            request, client_address = self.get_request()
        except OSError:
            return
        #然后马上通过verify_request验证用户的请求，这个方法可以重写，主要是验证客户端的IP端等需求
        if self.verify_request(request, client_address):
            try:
                #接下来通过在process_request调用finish_request方法中处理用户的请求
                self.process_request(request, client_address)
            except Exception:
                self.handle_error(request, client_address)
                self.shutdown_request(request)
            except:
                self.shutdown_request(request)
                raise
        else:
            self.shutdown_request(request)
```



```python
    #在process_request中分别执行了finish_request和shutdown_request
    def process_request(self, request, client_address):
        self.finish_request(request, client_address)
        self.shutdown_request(request)
```



首先看finish_request方法

```python
def finish_request(self, request, client_address):
    """Finish one request by instantiating RequestHandlerClass."""
    self.RequestHandlerClass(request, client_address, self)
```
代码中的RequestHandlerClass就是表示我们通过这行代码

```python
socketserver.ThreadingTCPServer(('127.0.0.1',8086),Server)
```

传入的Server参数类



也就是表示把参数request, client_address, self传入到我们自己编写的代码中，而我们的代码是继承于socketserver中的三个Handler类

socketserver模块提供了三个Handler类：

1、BaseRequestHandler

2、StreamRequestHandler

3、DatagramRequestHandler 

后两个是第一个的子类。直接使用BaseRequestHandler就行，但StreamRequestHandler、DatagramRequestHandler分别适合处理流式数据和数据报数据 

首先看BaseRequestHandler类

```python
class BaseRequestHandler:

    def __init__(self, request, client_address, server):
        self.request = request
        self.client_address = client_address
        self.server = server
        self.setup()
        try:
            self.handle()
        finally:
            self.finish()

    def setup(self):
        pass

    def handle(self):
        pass

    def finish(self):
        pass
```

其中包含了setup()是处理前的初始化操作，handle()是处理请求，finish()是清理操作三个方法，但是实现方法都是空的，所以直接使用BaseRequestHandler，你至少得重写handle()，然后根据需要决定是否重写setup()、finish()。于是我们的代码继承的是BaseRequestHandler，直接重写handle方法，用于处理请求



执行完process_request下的finish_request方法后，继续执行了shutdown_request方法

```python
    #该方法在完成了客户端请求后，调用close_request来关闭了客户端的连接
    def shutdown_request(self, request):
        """Called to shutdown and close an individual request."""
        self.close_request(request)
```

在执行完成serve_forever函数中的_handle_request_noblock方法后又继续执行了self.service_actions方法

```python
    def service_actions(self):
        pass
```

但是源码中的这个方法为空，可以用于当你执行完每一个客户端请求后，想要执行的逻辑操作，如计数+1等



