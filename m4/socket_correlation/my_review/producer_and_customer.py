import time
from multiprocessing import Process,JoinableQueue

def producer(name,q):
    for i in range(10):
        q.put('%s的第%s个包子'%(name,i))
        print('%s生产了第%s个包子'%(name,i))
    q.join()

def customer(name,q):
    while True:
        time.sleep(2)
        res = q.get()
        print('%s吃了%s'%(name,res))
        q.task_done()

if __name__ == '__main__':
    q = JoinableQueue()
    p1 = Process(target=producer,args=('小马',q))
    p2 = Process(target=producer,args=('小风',q))
    p3 = Process(target=producer,args=('小云',q))
    p1.start()
    p2.start()
    p3.start()

    c1 = Process(target=customer,args=('alex',q))
    c2 = Process(target=customer,args=('wxx',q))
    c1.daemon=True
    c2.daemon=True
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()

    print('主')