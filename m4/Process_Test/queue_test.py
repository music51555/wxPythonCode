import time

from multiprocessing import Process,JoinableQueue

def pruducer(name,q):
    for i in range(3):
        time.sleep(1)
        print('%s生产了%s个包子'%(name,i))
        q.put('%s的第%s个包子'%(name,i))
    q.join()

def customer(name,q):
    while True:
        time.sleep(2)
        res = q.get()
        print('%s 吃了 %s'%(name,res))
        q.task_done()

if __name__ == '__main__':
    q = JoinableQueue(2)
    p1 = Process(target = pruducer,args = ('生产者1',q))
    p2 = Process(target = pruducer,args = ('生产者2',q))
    p3 = Process(target = pruducer,args = ('生产者3',q))

    c1 = Process(target = customer,args = ('消费者1',q))
    c2 = Process(target = customer,args = ('消费者2',q))

    p1.start()
    p2.start()
    p3.start()

    c1.daemon = True
    c2.daemon = True

    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()

