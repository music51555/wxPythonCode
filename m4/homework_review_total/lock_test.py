# from multiprocessing import Process,Lock
# import time
#
# def task(name,mutex):
#     mutex.acquire()
#     print('%s is running'%name)
#     time.sleep(2)
#     print('%s is done'%name)
#     mutex.release()
#
# if __name__ == '__main__':
#     mutex = Lock()
#     p1 = Process(target = task,args = ('子进程1',mutex))
#     p2 = Process(target = task,args = ('子进程2',mutex))
#     p1.start()
#     p2.start()

from multiprocessing import Process,Lock
import json,time

def check_ticket(name):
    time.sleep(1)
    with open('ticket.json','r',encoding = 'utf-8') as f:
        ticket_dict = json.load(f)
        print('%s查询票数%s'%(name,ticket_dict['count']))

def buy_ticket(name):
    with open('ticket.json','r+',encoding = 'utf-8') as f:
        ticket_dict = json.load(f)
        if ticket_dict['count'] >= 1:
            ticket_dict['count'] -= 1
            time.sleep(2)
            print('%s购票成功'%name)
        else:
            print('%s购票失败'%name)
    with open('ticket.json','w',encoding = 'utf-8') as f:
        json.dump(ticket_dict,f)

def task(name,mutex):
    check_ticket(name)
    mutex.acquire()
    buy_ticket(name)
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    for i in range(10):
        p = Process(target = task,args = ('路人%s'%i,mutex))
        p.start()