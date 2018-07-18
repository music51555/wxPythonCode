from multiprocessing import Process,Lock
import json,time

class BuyTicket(Process):
    def __init__(self,name,mutex):
        super(BuyTicket,self).__init__()
        self.name = name
        self.mutex= mutex

    def run(self):
        self.check_ticket()
        self.mutex.acquire()
        self.buy_ticket()
        self.mutex.release()

    def check_ticket(self):
        time.sleep(1)
        ticket_dict = json.load(open('ticket_count.json','r',encoding = 'utf-8'))
        print('%s查询剩余%s张票'%(self.name,ticket_dict['ticket_count']))

    def buy_ticket(self):
        ticket_dict = json.load(open('ticket_count.json', 'r', encoding='utf-8'))
        if ticket_dict['ticket_count'] > 0:
            ticket_dict['ticket_count'] -= 1
            time.sleep(2)
            json.dump(ticket_dict, open('ticket_count.json', 'w', encoding='utf-8'))
            print('%s购票成功'%self.name)
        else:
            print('%s购票失败'%self.name)

if __name__ == '__main__':
    mutex = Lock()
    for i in range(5):
        p = BuyTicket('路人%s'%i,mutex)
        p.start()
