import time
from threading import Thread,Lock

n = 100

def task(mutex):
    global n
    mutex.acquire()
    temp = n
    time.sleep(0.1)
    n = temp - 1
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    t_l= []
    for i in range(100):
        t = Thread(target = task,args = (mutex,))
        t_l.append(t)
        t.start()

    for t in t_l:
        t.join()

    print('主',n)