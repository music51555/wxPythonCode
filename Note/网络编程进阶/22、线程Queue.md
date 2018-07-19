线程queue

**1、基础用法**

```python
#放入多少个，取多少个，先进先出
import queue

q = queue.Queue()
q.put('first')
q.put('twice')
q.put('third')

print(q.get())
print(q.get())
print(q.get())
'''
first
twice
third
'''
```



**1、block 阻塞状态**

block = True表示阻塞，block = False表示不阻塞

```python
from threading import Thread
import queue,time

def task(q):
    q.put('first')
    print('put first')
    q.put('second')
    print('put second')
    #当关闭阻塞状态时，就是你随便放入数据，但是如果满员了，就会报错“queue.Full”
    q.put('third',block = False)
    #当默认开启了阻塞状态时，表示有地方你才能放入数据，没有地方就等着。block = True，且timeout参数为None时，就会等待队列可放入数据，未满员状态时，去放入数据
    print('put third'，block = True)
    q.put('forth')
    print('put forth')

def foo(q):
    time.sleep(10)
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())

if __name__ == '__main__':
    q = queue.Queue(maxsize = 2)
    t1 = Thread(target = task,args = (q,))
    t2 = Thread(target = foo,args = (q,))

    t1.start()
    t2.start()
```

只有当默认情况下block = True的情况下，才使用timeout参数，如果添加了block = False，那么timeout参数没有用，因为源代码显示只有在block为True的时候才去判断timeout参数的状态

```python
                
    		   if not block:
                    if self._qsize() >= self.maxsize:
                        raise Full
                #只有在block为True的时候才去判断timeout参数的状态
                elif timeout is None:
                    while self._qsize() >= self.maxsize:
                        self.not_full.wait()
                elif timeout < 0:
                    raise ValueError("'timeout' must be a non-negative number")
                else:
                    endtime = time() + timeout
                    while self._qsize() >= self.maxsize:
                        remaining = endtime - time()
                        if remaining <= 0.0:
                            raise Full
                        self.not_full.wait(remaining)
```



**2、timeout**

```python
import queue

#如果队列没有满员，会直接放入数据
#如果队列满员后，等待3秒后放入数据，如果队列依然满员，则会报错full
q = queue.Queue(3)
q.put('first')
q.put('twice')
q.put('third')
q.put('forth',timeout = 3)

print(q.get())
print(q.get())
print(q.get())
```



**3、set_nowait()、get_nowait()**

```python
import queue

#put_nowait()和get_nowait()等同于put()和get()
q = queue.Queue(3)
q.put_nowait('first')
q.put_nowait('twice')
q.put_nowait('third')

print(q.get())
print(q.get())
print(q.get())
```



**4、q.LiFoQueue**

```python
import queue

#表示Last in First Out，后进先出，最后进入队列的，先get到
q = queue.LifoQueue(3)
q.put_nowait('first')
q.put_nowait('twice')
q.put_nowait('third')

print(q.get())
print(q.get())
print(q.get())
'''
third
twice
first
'''
```



**5、PriorityQueue** 

美 [praɪˈɔ:rəti] 优先级

```python
import queue

#按优先级get数据，数字越小，优先级越高
q = queue.PriorityQueue(3)
q.put((10,'first'))
q.put((30,'twice'))
q.put((20,'third'))

print(q.get())
print(q.get())
print(q.get())
```



**6、qsize**

q.qsiz（）输出队列中的成员数