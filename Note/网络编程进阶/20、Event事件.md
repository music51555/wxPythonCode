Event事件

在执行线程的过程中，如果其中某一线程需要根据其中一个线程的状态去执行代码，那么就会用到Event事件

```python
import time
from threading import Thread,current_thread,Event

t = Event()

def conn():
    n = 0
    while not t.is_set():
        if n == 3:
            print('连接服务端失败')
            return
        print('%s 正在尝试连接服务端,%s次'%(current_thread().getName(),n))
        time.sleep(1)
        n += 1
        continue
    #在线程执行的过程中，将线程的信号标识t.wait()状态设置为False，导致不能向下执行，当其他线程执行了t.set()方法后，才将该状态设置为True，可以向下执行
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

