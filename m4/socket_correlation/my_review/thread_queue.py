import queue,time
from threading import Thread

def task(q):
    q.put((1,1))
    q.put((3,2))
    q.put((2,3))
    print(q.qsize())

def foo(q):
    print(q.get())
    print(q.get())
    print(q.get())

if __name__ == '__main__':
    q = queue.PriorityQueue(maxsize=3)
    t1 = Thread(target=task,args=(q,))
    t2 = Thread(target=foo,args=(q,))
    t1.start()
    t2.start()