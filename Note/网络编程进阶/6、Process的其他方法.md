**join方法：**

主进程必须等待子进程执行完毕后，再运行主进程

```python
import time
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,name):
        super(MyProcess,self).__init__()
        self.name = name

    def run(self):
        print('%s is running'%self.name)
        time.sleep(2)
        print('%s is done'%self.name)

if __name__ == '__main__':
    p = MyProcess('子进程1')
    p.start()
    
    #添加join方法后主进程需要等待子进程执行完毕后，再执行，join方法是针对主进程的
    p.join()
    print('主进程')
'''
子进程1 is running
子进程1 is done
主进程
'''
```



并发执行start()方法，只是向操作系统发送信号，准备开启子进程，p1、p2、p3通过start()方法依次向操作系统发送信号，准备开启进程，p1发起请求后，CPU很快响应开启了进程，执行了run方法，而子进程2、子进程3发起了请求，操作系统系统还没有创建进程，就执行了主进程

```python
if __name__ == '__main__':
    p1 = MyProcess('子进程1')
    p2 = MyProcess('子进程2')
    p3 = MyProcess('子进程3')

    p1.start()
    p2.start()
    p3.start()
    print('主进程')
'''
子进程1 is running
主进程
子进程2 is running
子进程3 is running
'''
#当遇到先执行了主程序，是因为子进程1、2、3都发送了开启进程的请求，但操作系统都没有来得及开启时，就执行到了执行主进程的代码，所以先开执行了主进程
'''
主进程
子进程1 is running
子进程2 is running
子进程3 is running
'''
```



子进程1、2、3发送信号后，如果子进程1的执行时间是5秒，子进程2是3秒，子进程3是1秒的话，那么当添加join方法后，主进程的等待最长时间是5秒，因为在执行子进程1的5秒时间内，子进程2和3都执行完毕了，start方法并不是依次执行子进程，而是都发送了开启进程的信号后，操作系统响应后创建进程进程，也可以简写为for循环的形式

```python
import time
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,name,n):
        super(MyProcess,self).__init__()
        self.name = name
        self.n = n

    def run(self):
        print('%s is running'%self.name)
        time.sleep(self.n)
        print('%s is done'%self.name)

if __name__ == '__main__':
    p1 = MyProcess('子进程1',5)
    p2 = MyProcess('子进程2',3)
    p3 = MyProcess('子进程3',2)

    p1.start()
    p2.start()
    p3.start()
    print('主进程')
#全程等待了5秒
'''
主进程
子进程1 is running
子进程2 is running
子进程3 is running
子进程3 is done
子进程2 is done
子进程1 is done
'''
```



那么如何实现依次执行子进程1、2、3呢，实在每次执行start前，都添加join方法，主进程等待子进程1、2、3执行完毕后，再次执行主进程

```python
if __name__ == '__main__':
    p1 = MyProcess('子进程1',5)
    p2 = MyProcess('子进程2',3)
    p3 = MyProcess('子进程3',2)

    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()
    print('主进程')
#每个进程都添加了join方法，所以主进程需要等待所有子进程执行完毕后才能执行，一共等待了10秒，但是这样做是没有意义的，开进程的目的就是为了实现并发
'''
子进程1 is running
子进程1 is done
子进程2 is running
子进程2 is done
子进程3 is running
子进程3 is done
主进程
'''
```



**is_alive**

可以验证进程是死的还是活的

```python
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,name):
        super(MyProcess,self).__init__()
        self.name = name

    def run(self):
        print('%s is running'%self.name)
        print('%s is done'%self.name)

if __name__ == '__main__':
    p1 = MyProcess('子进程1')

    p1.start()
    print(p1.is_alive())
    p1.join()
    print('主进程')
    print(p1.is_alive())
#子进程运行完毕后，通过is_alive()方法查看子进程，子进程已经结束了
'''
True
子进程1 is running
子进程1 is done
主进程
False
'''
```



**terminal**

可以让系统回收进程资源，进程被回收后不会被执行

```python
import time

from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,name):
        super(MyProcess,self).__init__()
        self.name = name

    def run(self):
        print('%s is running'%self.name)
        print('%s is done'%self.name)

if __name__ == '__main__':
    p1 = MyProcess('子进程1')

    p1.start()
    #只有在发起开进程的信号后，才可以使用terminate方法回收了子进程，所以输出的子进程状态都是False，也有可能在刚回收时，进程的状态还是True，子进程的函数内容也没有打印
    p1.terminate()
    time.sleep(2)
    print(p1.is_alive())
    p1.join()
    print('主进程')
    print(p1.is_alive())
'''
False
主进程
False
'''
```



**pid、name**

通过pid和name方法，查看进程的名称和pid，如果执行的name属性，会显示自定义的进程名称

```python
import time

from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,name):
        super(MyProcess,self).__init__()
        self.name = name

    def run(self):
        print('%s is running'%self.name)
        print('%s is done'%self.name)

if __name__ == '__main__':
    p1 = MyProcess('子进程1')

    p1.start()
    print(p1.pid)
    print(p1.name)
#得到了子进程的pid号和进程名称
'''
1829
子进程1
子进程1 is running
子进程1 is done
'''
```

