# from multiprocessing import Process
# import time
#
# def task(name):
#     print('%s is running'%name)
#     time.sleep(2)
#     print('%s is done'%name)
#
# if __name__ == '__main__':
#     p = Process(target = task,args = ('子进程',))
#     p.start()

# from multiprocessing import Process
# import time
#
# class ProcessTest(Process):
#
#     def __init__(self,name):
#         super(ProcessTest,self).__init__()
#         self.name = name
#
#     def run(self):
#         print('%s is running'%self.name)
#         time.sleep(2)
#         print('%s is done'%self.name)
#
# if __name__ == '__main__':
#     p = ProcessTest('子进程')
#     p.start()


# from multiprocessing import Process
# import time,os
#
# def task(name):
#     print('%s is running,it is pid %s'%(name,os.getpid()))
#     time.sleep(2)
#     print('%s is done'%name)
#
# if __name__ == '__main__':
#     p1 = Process(target = task,args = ('子进程1',))
#     p2 = Process(target = task,args = ('子进程2',))
#
#     p1.start()
#     p2.start()
#
#     print('主')

# from multiprocessing import Process
# import time,os
#
# class MyProcess(Process):
#
#     def __init__(self,name):
#         super(MyProcess,self).__init__()
#         self.name = name
#
#     def run(self):
#         print('%s is running,it is pid %s,it is ppid %s'%(self.name,os.getpid(),os.getppid()))
#         time.sleep(2)
#         print('%s is done'%self.name)
#
# if __name__ == '__main__':
#     m1 = MyProcess('子进程1')
#     m2 = MyProcess('子进程2')
#
#
#     m1.start()
#     m1.terminate()
#     print(m1.is_alive())
#     m2.start()
#
#     m1.join()
#     m2.join()
#     print(m1.is_alive())
#
#     print('主')

from multiprocessing import Process

class MyProcess(Process):

    def run(self):
        print(' is running')

if __name__ == '__main__':
    m = MyProcess(name = '子进程')
    m.start()
    print(m.pid)
    print(m.name)


