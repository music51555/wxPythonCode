from multiprocessing import Process,Queue
import time

def task(q):
    q.put(1,block =False)
    print('put 1')
    q.put(2)
    print('put 2')
    q.put(3)
    print('put 3')

def foo(q):
    time.sleep(10)
    print(q.get())
    print(q.get())
    print(q.get())

if __name__ == '__main__':
    q = Queue(maxsize=2)
    p1 = Process(target = task,args = (q,))
    p2 = Process(target = foo,args = (q,))

    p1.start()
    p2.start()
