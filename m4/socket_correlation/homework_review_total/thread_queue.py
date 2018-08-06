from threading import Thread
import queue,time

def task(q):
    q.put((1,'first'))
    print('put first')
    q.put((3,'second'))
    print('put second')
    q.put((2,'third'),timeout = 3)
    print('put third')
    print(q.qsize())

def foo(q):
    time.sleep(5)
    print(q.get())
    print(q.get())
    print(q.get())

if __name__ == '__main__':
    q = queue.PriorityQueue()
    t1 = Thread(target = task,args = (q,))
    t2 = Thread(target = foo,args = (q,))

    t1.start()
    t2.start()