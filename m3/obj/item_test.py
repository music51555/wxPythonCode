class Foo:
    def __init__(self,school):
        self.school = school

    def study(self):
        print('is studying')

    def talk(self):
        print('is talking')

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        print('key',key)
        print('value',value)
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]
        print(self.__dict__)

f = Foo('北大青鸟')
print(f['school'])

f['school'] = '慕课网'
print(f['school'])

del f['school']