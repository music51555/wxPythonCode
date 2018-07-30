from threading import Thread,Lock,current_thread
import time

n = 100

def task(mutex):
    global n
    mutex.acquire()
    temp = n
    temp -= 1
    n = temp
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    t_l = []
    for i in range(100):
        t = Thread(target = task,args = (mutex,))
        t_l.append(t)
        t.start()

    for i in t_l:
        i.join()

    print('n',n)

