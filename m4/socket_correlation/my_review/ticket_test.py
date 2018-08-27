import json
import time
from multiprocessing import Process,Lock

def search_ticket(name):
    time.sleep(1)
    f = open('ticket.json','r')
    total_ticket = json.load(f)
    print('%s查询票数剩余%s'%(name,total_ticket['ticket']))

def buy_ticket(name):
    f = open('ticket.json','r')
    total_ticket = json.load(f)
    if total_ticket['ticket']>0:
        total_ticket['ticket'] -= 1
        print('%s购票成功'%name)
    else:
        print('%s购票失败'%name)
    time.sleep(2)
    f = open('ticket.json','w')
    json.dump(total_ticket,f)

def task(name,mutex):
    search_ticket(name)
    mutex.acquire()
    buy_ticket(name)
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    for i in range(10):
        p1 = Process(target=task,args=('路人%s'%i,mutex))
        p1.start()