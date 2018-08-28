import time,os
from threading import Thread
from multiprocessing import Process

def task():
    res = 1
    for i in range(1000000):
        res *= i

if __name__ == '__main__':
    start = time.time()
    p_l = []
    t_l = []
    for i in range(os.cpu_count()):
        # p = Process(target=task) #5.192296981811523
        # p.start()
        # p_l.append(p)
        t = Thread(target=task)
        t.start()
        t_l.append(t)

    # for p in p_l:
    #     p.join()
    for t in t_l:
        t.join()

    end = time.time()
    print(end - start)


