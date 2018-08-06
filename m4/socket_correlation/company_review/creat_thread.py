# import time
# import os
# from threading import Thread,current_thread
#
# def task():
#     print('%s is running,it is pid %s'%(current_thread().getName(),os.getpid()))
#     time.sleep(2)
#     print('%s is done'%current_thread().getName())
#
# if __name__ == '__main__':
#     t = Thread(target = task,name = '子线程')
#     t.start()
#
#     print('主线程，pid是%s'%os.getpid())

from threading import Thread,current_thread
import time,os

class MyThread(Thread):
    def run(self):
        print('%s is running,it is pid %s' % (current_thread().getName(), os.getpid()))
        time.sleep(2)
        print('%s is done'%current_thread().getName())

if __name__ == '__main__':
    m = MyThread()
    m.setName('子线程')
    m.start()