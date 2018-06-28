# class People:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def talk(self):
#         print(self.name+' is talking')
#
# p = People('alex',20)
# p.talk()
# People.talk(p)

# class foo:
#     def f1(self):
#         print('from foo.f1')
#         self.f2()      #4、此时的self表示对象本身，于是从对象本身的类中查找f2函数
#     def f2(self):      #3、最后依次从父类中查找
#         print('from foo.f2')
#
# class bar(foo):
#     def f2(self):      #2、再从实例化的类中查找
#         print('from bar.f2')
# b1 = bar()
# b1.f1()
# print(foo.__bases__)
# import
# class A:
#     def func1(self):
#         print('from A')
#         print(super())
#         super().func1()
#
# class B:
#     def func1(self):
#         print('from B')
#
# class C(A,B):
#     pass
#
# c = C()
# c.func1()
# print(C.mro())

class Foo:
    __school = 'LuffySchool'

    def __study(self):
        print('Foo is studying')

    def eat(self):      #Bar类中没有eat方法，于是在父类中查看，当遇到self.__study()时，由于__study是在类定义阶段就已经变为_Foo_study，所以访问的是Foo类中的__study函数，所以只能访问本类中的__变量属性
        print('Foo is eating')
        self.__study()

class Bar(Foo):
    def __eat(self):
        print('Bar is studying')

b = Bar()
b.eat()