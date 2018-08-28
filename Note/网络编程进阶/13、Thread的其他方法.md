Thread的其他方法

**1、getName**

引入from threading import current_thread()，表示当前线程

```python
import time,os
from threading import Thread,current_thread

def task(name):
    print('%s is running'%(name))
    time.sleep(2)
    #未通过name参数设置线程名称时，默认为Thread-1
    print('it is name %s'%current_thread().getName())

if __name__ == '__main__':
    t = Thread(target = task,args = ('子进程1',))
    t.start()
    print('主线程')
#current_thread表示当前主线程的对象，通过对象可以调用getName()来获取线程名称
'''
子进程1 is running
主线程
it is name Thread-1
'''
```



**2、setName**

创建线程时

1、可以通过name参数设置线程名

2、或通过线程对象.setName()来设置线程名

```python
from threading import Thread,current_thread

def task():
    print('子线程的名字是%s'%current_thread().getName())

if __name__ == '__main__':
    #1、可以通过name参数设置子线程的名称
    t = Thread(target = task,name = '子进程')
    #2、或者通过线程对象的setName方法来设置子线程的名称
    t.setName('子进程1')
    t.start()
    print('主线程')
```



**3、is_alive**

和进程一样，线程也有is_alive方法，用于判断进程的状态，是否存活

```python
import time

from threading import Thread,current_thread

def task():
    print('子线程的名字是%s'%current_thread().getName())
    time.sleep(2)

if __name__ == '__main__':
    t = Thread(target = task)
    t.setName('子进程1')
    #通过is_alive()方法查看子进程的状态，True表示alive，False表示dead
    print(t.is_alive())
    t.start()
    #在子进程发起信号并启动后，子进程的状态为True
    print(t.is_alive())
    print('主线程')
```



**4、active_count**

活跃线程数，从threading中引入active_count，打印active_count()来输出当前活跃的进程数

```python
import time

from threading import Thread,current_thread,active_count

def task():
    print('子线程的名字是%s'%current_thread().getName())
    time.sleep(2)

if __name__ == '__main__':
    t = Thread(target = task)
    t.setName('子进程1')
    t.start()
    #引入active_count方法后，调用该方法，输出当前活跃的线程数
    print(active_count())
    print('主线程')
```



**5、enumerate**

活跃线程对象，和is_alive()一样，也是从threading中引入enumerate类，使用enumerate()打印当前活跃的线程对象

```python
import time

from threading import Thread,current_thread,enumerate

def task():
    print('子线程的名字是%s'%current_thread().getName())
    time.sleep(2)

if __name__ == '__main__':
    t = Thread(target = task)
    t.setName('子进程1')
    t.start()
    print(enumerate())
    print('主线程')
#通过enumerate方法，得到当前活跃线程数的对象
'''
子线程的名字是子进程1
[<_MainThread(MainThread, started 140735103569920)>, <Thread(子进程1, started 123145307557888)>]
主线程
'''
```



