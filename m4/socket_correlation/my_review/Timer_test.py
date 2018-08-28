# from threading import Thread,Timer,current_thread
#
# def task():
#     t = Timer(interval=5,function=task)
#     t.start()
#     print('hello world,thread name is %s'%current_thread().getName())
#
# if __name__ == '__main__':
#     task()

import random,string
from threading import Thread,Timer

class Input_Code():
    def refresh_code(self):
        t = Timer(interval=5,function=self.refresh_code)
        t.start()
        self.code = ''.join(random.sample(string.ascii_lowercase+string.ascii_uppercase,4))

    def check_code(self):
        while True:
            print(self.code)
            msg = input('>>>:')
            if msg==self.code:
                print('success')
            else:
                print('fail')

if __name__ == '__main__':
    i = Input_Code()
    i.refresh_code()
    i.check_code()