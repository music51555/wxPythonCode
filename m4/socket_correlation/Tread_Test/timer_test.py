from threading import Timer
import string,random,time

class ReCode:
    def make_code(self):
        self.code = ''.join(random.sample(string.ascii_lowercase+string.ascii_uppercase,4))
        t = Timer(interval = 5,function = self.make_code)
        t.start()

    def in_code(self):
        while True:
            print(self.code)
            msg = input('>>>:')
            if msg == self.code:
                print('输入正确')
            else:
                print('输入错误')

if __name__ == '__main__':
    r = ReCode()
    r.make_code()
    r.in_code()