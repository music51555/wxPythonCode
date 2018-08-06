# from threading import Thread
#
# def task(name):
#     print('%s is running'%name)
#
# if __name__ == '__main__':
#     t = Thread(target = task,args = ('子进程1',))
#     t.start()
#
#     print('主线程')

import time
from threading import Thread

class MyThread(Thread):
    def __init__(self,name):
        super(MyThread,self).__init__()

    def run(self):
        print('%s is running'%self.name)
        time.sleep(2)
        print('%s is done'%self.name)

if __name__ == '__main__':
    m = MyThread('子线程1')
    m.start()

    print('主线程')