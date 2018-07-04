class Foo(object):

    def __init__(self, list):
        print(list)
        self.list = list

    def __iter__(self):
        return iter(self.list)

obj = Foo([11,22,33,44])

for i in obj:
    print(i)