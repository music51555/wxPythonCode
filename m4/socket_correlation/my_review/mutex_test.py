import time
from threading import Thread,RLock

mutexA = mutexB = RLock()

def task():
    mutexA.acquire()
    print('task得到A锁')
    time.sleep(1)
    mutexB.acquire()
    print('task得到B锁')
    mutexA.release()
    mutexB.release()

def foo():
    mutexB.acquire()
    print('foo得到B锁')
    time.sleep(1)
    mutexA.acquire()
    print('foo得到A锁')
    mutexB.release()
    mutexA.release()

if __name__ == '__main__':
    t1 = Thread(target=task)
    t2 = Thread(target=foo)
    t1.start()
    t2.start()