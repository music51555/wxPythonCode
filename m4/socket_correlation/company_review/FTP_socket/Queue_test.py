#简单实现队列
from multiprocessing import Process,JoinableQueue
import time

def producter(name,q):
    for i in range(5):
        time.sleep(0.5)
        print('%s生产了第%s个包子'%(name,i))
        q.put('%s生产了第%s个包子'%(name,i))
    q.join()

def customer(name,q):
    while True:
        res = q.get()
        time.sleep(1)
        if not res:
            break
        print('%s吃了%s'%(name,res))
        q.task_done()

if __name__ == '__main__':
    q = JoinableQueue()
    p1 = Process(target = producter,args = ('alex',q))
    p2 = Process(target = producter,args = ('peiqi',q))
    p3 = Process(target = producter,args = ('egon',q))
    c1 = Process(target = customer,args = ('小明',q))
    c2 = Process(target = customer,args = ('小红',q))

    c1.daemon = True
    c2.daemon = True
    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()