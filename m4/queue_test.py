import time

from multiprocessing import Process,JoinableQueue

def producer(name,q):
    for i in range(2):
        q.put(i)
        print('%s 生产了%s包子'%(name,i))
        time.sleep(1)
    q.join()

def customer(name,q):
    while True:
        time.sleep(2)
        res = q.get()
        print('%s吃了%s包子'%(name,res))
        q.task_done()

if __name__ == '__main__':
    q = JoinableQueue()
    p1 = Process(target = producer,args = ('生产者1',q))
    p2 = Process(target = producer,args = ('生产者2',q))
    p3 = Process(target = producer,args = ('生产者3',q))
    c1 = Process(target = customer,args = ('消费者1',q))
    c2 = Process(target = customer,args = ('消费者2',q))

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
    print('主进程')