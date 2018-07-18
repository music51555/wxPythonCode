from multiprocessing import Process
import time,os

def task():
    print('开始执行子进程,pid是%s'%os.getpid())
    time.sleep(50)
    print('子进程执行完毕')

if __name__ == '__main__':
    p = Process(target = task)
    p.start()

    print('主进程，pid是%s'%os.getpid())

# from threading import Thread
# import time,os
#
# def task():
#     print('开始执行子线程，pid是%s'%os.getpid())
#     time.sleep(60)
#     print('子线程执行完毕')
#
# if __name__ == '__main__':
#     t = Thread(target = task)
#     t.start()
#
#     print('主线程pid是%s'%os.getpid())