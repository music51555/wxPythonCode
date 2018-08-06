from threading import Semaphore,current_thread,Thread
import time

def task(mutex):
    mutex.acquire()
    print('%s is running'%current_thread().getName())
    time.sleep(2)
    print('%s is done'%current_thread().getName())
    mutex.release()

if __name__ == '__main__':
    mutex = Semaphore(5)
    for i in range(10):
        t = Thread(target = task,args = (mutex,))
        t.start()