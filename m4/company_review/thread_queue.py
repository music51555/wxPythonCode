from threading import Thread
import queue,time

def task(q):
    q.put('first')
    print('put first')
    q.put('second')
    print('put second')
    q.put('third')
    print('put third')
    q.put('forth')
    print('put forth')

def foo(q):
    time.sleep(10)
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())

if __name__ == '__main__':
    q = queue.LifoQueue(maxsize = 2)
    t1 = Thread(target = task,args = (q,))
    t2 = Thread(target = foo,args = (q,))

    t1.start()
    t2.start()