class calc:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,val):
        self.__name = val

    @name.deleter
    def name(self):
        print('不允许删除')

c = calc('alex')
print(c.name)
c.name = 'peiqi'
print(c.name)
del c.name

