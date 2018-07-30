from threading import Thread,Timer
import random,string,time

class InCode():
    def make_code(self):
        self.code = ''.join(random.sample(string.ascii_lowercase + string.ascii_uppercase,4))
        t = Timer(interval = 5,function = self.make_code)
        t.start()

    def check_code(self):
        while True:
            print(self.code)
            code = input('>>>:')
            if code == self.code:
                print('succcess')
            else:
                print('fail')

if __name__ == '__main__':
    i = InCode()
    i.make_code()
    i.check_code()

