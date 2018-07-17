import string,random
from threading import Thread,Timer

class In_Code:
    def __init__(self):
        self.make_code()

    def make_code(self):
        code = ''.join(random.sample(string.ascii_lowercase + string.ascii_uppercase,4))
        return code

    def verify_code(self):
        self.cache_code = self.make_code()
        t = Timer(interval = 5,function = self.verify_code)
        t.start()

    def check(self):
        while True:
            print(self.cache_code)
            input_code = input('请输入验证码>>>：').strip()
            if input_code == self.cache_code:
                print('输入正确')
                continue

if __name__ == '__main__':
    i = In_Code()
    i.verify_code()
    i.check()