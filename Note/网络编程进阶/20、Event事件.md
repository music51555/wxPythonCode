Event事件

**简单的实现Event事件，涉及的方法set()和wait()**

```python
#Event事件本质是通过wait方法设置等待状态，其他线程通过set方法发送给wait通知，让wait方法不必继续等待，可以执行后面的代码了
from threading import Thread,Event
import time

def task(e):
    print('客户端：可以连接了吗？，当前连接状态是%s'%e.is_set())
    e.wait()
    print('客户端：好啦，我连接成功')

def check(e):
    print('服务端：还不行，服务器设置了3秒等待时间')
    time.sleep(3)
    e.set()
    print('服务端：可以连接了,设置连接状态为%s'%e.is_set())

if __name__ == '__main__':
    e = Event()
    t1 = Thread(target = task,args = (e,))
    t2 = Thread(target = check,args = (e,))

    t1.start()
    t2.start()
'''
客户端：可以连接了吗？，当前连接状态是False
服务端：还不行，服务器设置了3秒等待时间
服务端：可以连接了,设置连接状态为True
客户端：好啦，我连接成功
'''
```



在执行线程的过程中，如果其中某一线程需要根据其中一个线程的状态去执行代码，那么就会用到Event事件

**实际的socket套接字连接实例**

多了一个is_set()方法，判断是否执行了set()方法，True和False

```python
import time
from threading import Thread,current_thread,Event

t = Event()

def conn():
    n = 0
    #其中is_set表示当前的状态，默认为Flase，表示让wait等待，set完成后，变为True，告诉wait不必等待
    while not t.is_set():
        if n == 3:
            print('连接服务端失败')
            return
        print('%s 正在尝试连接服务端,%s次'%(current_thread().getName(),n))
        time.sleep(1)
        n += 1
        continue
    #在线程执行的过程中，将线程的信号标识t.wait()状态设置为False，导致不能向下执行，当其他线程执行了t.set()方法后，才将该状态设置为True，可以向下执行，在此可以设置超时等待时间，如果过了等待时间，函数还没有set的话，就会向下执行
    t.wait()
    print('%s 连接成功'%current_thread().getName())

def check():
    print('正在检查服务端连接...')
    time.sleep(2)
    print('您可以连接服务端了')
    t.set()

if __name__ == '__main__':
    t1 = Thread(target = check)
    t2 = Thread(target = conn,name = '客户端')

    t1.start()
    t2.start()
'''
正在检查服务端连接...
客户端 正在尝试连接服务端,0次
客户端 正在尝试连接服务端,1次
您可以连接服务端了
客户端 连接成功
'''
```



**总结：**

Event方法包含set、wait、is_set方法3种方法，set方法用于告知wait方法可以执行后续的代码，is_set方法用于判断是否执行了set方法

Event可以既可以用于进程，也可以用于线程