multiprocessing中的Array和Value

无论是value还是Array，数据都是共享于所有进程的

**Value类：**

```python
from multiprocessing import Process,Value
import time

def task(name):
    time.sleep(5)
    #在task中打印了在foo中经过计算的res.value
    print('%s is running,value is %s'%(name,res.value))

def foo(name):
    #在foo中修改了res对象value值
    res.value -= 100
    print('%s is running,value is %s'%(name,res.value))

if __name__ == '__main__':
    #value是作用于全局的，相当于开启了一块进程间的共享内存，i表示整形参数
    res = Value('i',2000)

    p1 = Process(target = task,args = ('子进程1',))
    p2 = Process(target = foo,args = ('子进程2',))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```



**Array类：**

```python
from multiprocessing import Process,Array
import time

def task(name):
    print('%s is running'%(name,))
    #分别在task和foo中插入数据，在最后进行打印
    for i in range(3):
        m[i] = i

def foo(name):
    time.sleep(5)
    print('%s is running'%(name,))
    for i in range(3,5):
        m[i] = i

if __name__ == '__main__':
    #i参数数值类型，5表示开启的数组空间，可以存放多少个值
    m = Array('i',5)
    p1 = Process(target = task,args = ('子进程1',))
    p2 = Process(target = foo,args = ('子进程2',))
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(m[:])
'''
子进程1 is running
子进程2 is running
[0, 1, 2, 3, 4]
'''
```



**Manager类**

也是用于进程间通信的

```python
from multiprocessing import Process,Manager
import time

def task(d):
    d.append('haha')

def foo(d):
    time.sleep(2)
    print(d)

if __name__ == '__main__':
    m = Manager()
    d = m.list()
    p1 = Process(target = task,args = (d,))
    p2 = Process(target = foo,args = (d,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
'''
['haha']
'''
```

