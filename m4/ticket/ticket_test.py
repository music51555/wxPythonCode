import json
import time
from multiprocessing import Process,Lock

def search(name):
    time.sleep(1)
    ticket_dict = json.load(open('ticket.txt','r',encoding = 'utf-8'))
    print('%s开始查票,剩余票数%s'%(name,ticket_dict['ticket_count']))

def buy_ticket(name):
    ticket_dict = json.load(open('ticket.txt','r',encoding = 'utf-8'))
    if ticket_dict['ticket_count'] > 0:
        ticket_dict['ticket_count'] -= 1
        time.sleep(2)
        json.dump(ticket_dict,open('ticket.txt','w'))
        print('%s购票成功'%name)

def task(name,mutex):
    search(name)
    mutex.acquire()
    buy_ticket(name)
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    for i in range(11):
        p = Process(target = task,args = ('路人%s'%i,mutex))
        p.start()