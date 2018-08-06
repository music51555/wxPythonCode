# from multiprocessing import Process
# from threading import Thread
# import os,time
# def work():
#     res=0
#     for i in range(100000000):
#         res*=i
#
# if __name__ == '__main__':
#     l=[]
#     start = time.time()
#     for i in range(8):
#         # p = Process(target=work) #用时10秒
#         p = Thread(target=work) #用时47秒
#         l.append(p)
#         p.start()
#
#     for p in l:
#         p.join()
#
#     stop = time.time()
#     print('run time is %s' %(stop - start))

from multiprocessing import Process
from threading import Thread
import threading
import os,time
def work():
    time.sleep(2)
    print('===>')

if __name__ == '__main__':
    l=[]
    print(os.cpu_count()) #本机为4核
    start=time.time()
    for i in range(400):
        # p=Process(target=work)   #用时3.02秒
        p=Thread(target=work)  #用时2.4秒
        l.append(p)
        p.start()

    for p in l:
        p.join()

    stop=time.time()
    print('run time is %s' %(stop-start))