from multiprocessing import Process,current_process,Lock
import time,os,random
n = 100

def task(name,mutex):
    global n
    mutex.acquire()
    temp = n
    n = temp - 1
    print('%s is running,it is pid %s,n = %s' % (name, current_process().pid,n))
    time.sleep(random.randint(1,3))
    print('%s is done'%name)
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    p_l = []
    for i in range(3):
        p = Process(target = task,args = ('子进程%s'%i,mutex))
        p_l.append(p)
        p.start()

    print('主进程,n = %s'%n)

# from multiprocessing import Process
# import time,os

# class MyProcess(Process):
#     def __init__(self,name):
#         super(MyProcess,self).__init__()
#         self.name = name
#
#     def run(self):
#         print('%s is running,it is pid %s，it is parentpid is %s' % (self.name, os.getpid(),os.getppid()))
#         time.sleep(2)
#         print('%s is done'%self.name)
#
# if __name__ == '__main__':
#     p = MyProcess('子进程')
#     p.start()
#
#     print('主进程的PID是%s'%os.getpid())
