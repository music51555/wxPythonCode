# import time
#
# from multiprocessing import Process
#
# def task(name):
#     print('%s is running'%name)
#     time.sleep(2)
#     print('%s is done'%name)
#
# if __name__ == '__main__':
#     # p = Process(target = task,kwargs = {'name':'子进程1'})
#     p = Process(target = task,args = ('子进程1',))
#     p.start()
#
#     print('主')

import time
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,name):
        super(MyProcess,self).__init__()
        self.name = name

    #方法名必须写为run
    def run(self):
        print('%s is running'%self.name)
        time.sleep(2)
        print('%s is done'%self.name)

if __name__ == '__main__':
    p = MyProcess('子进程1')
    #start本质调用的就是绑定方法run
    p.start()

    print('主')
