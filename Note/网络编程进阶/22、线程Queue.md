线程queue

**1、基础用法**

```python
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
import queue

#设置队列数为3，放满3个数据后，再次以不阻塞的状态放入数据，程序会报错“queue.Full”
q = queue.Queue(3)
q.put('first',block = True)
q.put('twice',block = True)
q.put('third',block = True)
q.put('forth',block = False)

print(q.get())
print(q.get())
print(q.get())
```



**2、timeout**

```python
import queue

#队列埋怨后，等待3秒后放入数据，如果队列依然满员，则会报错full
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




