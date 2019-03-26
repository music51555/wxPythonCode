class TestClassMethod:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def greeting(cls,name):
        print('hello world%s'%name)

    @staticmethod
    def good_night():
        print('good night')

    def good_morning(self):
        print('good_morning {},you age {}'.format(self.name,self.age))

if __name__ == '__main__':
    TestClassMethod.greeting('alex')
    TestClassMethod.good_night()
    TestClassMethod('alex', 30).greeting('alex')
    TestClassMethod('alex', 30).good_night()

    TestClassMethod('alex',30).good_morning()
