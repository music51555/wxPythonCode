from threading import Thread,RLock
import time

mutex = RLock()

def task():
    mutex.acquire()
    print('task A')
    time.sleep(2)
    mutex.acquire()
    print('task B')
    mutex.release()
    mutex.release()

def foo():
    mutex.acquire()
    print('foo B')
    mutex.acquire()
    print('foo A')
    mutex.release()
    mutex.release()

if __name__ == '__main__':
    t1 = Thread(target = task)
    t2 = Thread(target = foo)

    t1.start()
    t2.start()

    print('主')