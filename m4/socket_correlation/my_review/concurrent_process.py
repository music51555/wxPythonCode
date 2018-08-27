# import time
# import os
# from multiprocessing import Process
#
# def task(name):
#     print('%s is running,it is pis %s,it is parent pid %s'%(name,os.getpid(),os.getppid()))
#     time.sleep(2)
#     print('%s is done'%name)
#
# if __name__ == '__main__':
#     p1 = Process(target=task,args=('子进程1',))
#     p1.start()
#
#     p2 = Process(target=task,args=('子进程2',))
#     p2.start()

import time
import os
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,name):
        super(MyProcess,self).__init__()
        self.name = name

    def run(self):
        print('%s is running,it is pid %s,parent pid %s'%(self.name,os.getpid(),os.getppid()))
        time.sleep(2)
        print('%s is done'%self.name)

if __name__ == '__main__':
    m1 = MyProcess('子进程1')
    m1.daemon=True
    m1.start()

    m2 = MyProcess('子进程2')
    m2.start()

    print('主')
