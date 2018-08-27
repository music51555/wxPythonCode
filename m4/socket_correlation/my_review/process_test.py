# import time
# from multiprocessing import Process
#
# def task(name):
#     print('%s is running'%name)
#     time.sleep(2)
#     print('%s is done'%name)
#
# if __name__ == '__main__':
#     p = Process(target=task,args=('子进程1',))
#     p.start()

import time
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,name):
        super(MyProcess,self).__init__()
        self.name=name

    def run(self):
        print('%s is running'%self.name)
        time.sleep(2)
        print('%s is done'%self.name)

if __name__=='__main__':
    m = MyProcess('子进程1')
    m.start()