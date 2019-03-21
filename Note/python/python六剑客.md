**`lambda`表达式**

`lambda`相当于定义一个函数

```python
# 将lambda表达式赋值给变量ret，以后可以通过变量调用lambda函数
# lambda x表示定义一个匿名函数，x表示传入函数的形参
# 冒号：后的表示函数执行的代码块
ret = lambda x:x*x

print(ret(2))
print(ret(5))
print(ret(3))
```

**`lambda`扩展**

通过列表的`sort`方法，对列表中的元祖，按元祖索引排序；对列表中的字典，按`value`值进行排序

```python
# 如果是列表单纯的排序，直接调用列表片的sort方法即可，无需key，
s = [2,1,5,1,23,1]
s.sort()
print(s)

# key是针对于列表中的元祖或字典排序时使用的，且key必须接收的是一个函数
names = [(1,3,2),(3,1,1),(1,4,0),(2,5,5),(2,1,10)]
names.sort(key=lambda names:names[2])
print(names)

# 字典排序使用dict.items，将字典每一个key和value变为(key,value)形式
name_dict = {'name1':'alex','name2':'mary','name3':'bob'}
new_dict = sorted(name_dict.items(),key=lambda item:item[1])
print(new_dict)

# key是针对于列表中的元祖或字典排序时使用的，且key必须接收的是一个函数
names = [{'name':'zero'},{'name':'alex'},{'name':'mary'},{'name':'bob'}]
names.sort(key=lambda names:names['name'])
print(names)
```



`map`

map的作用实际上是将一个可迭代的对象，传入到`func`函数中，进行运算，返回一个列表结果

说通俗点就是将可迭代对象中的元素依次传入到`func`函数中，进行**单个处理**

![1553134296062](.\images\1553134296062.png)

```python
# 最基础的使用方法
ret = map(lambda x:x**2,[1,2,3,4,5])
print(list(ret))
[1, 4, 9, 16, 25]
```





`reduce`

将集合中的每一个元素依次传入`reduce`中进行**相互处理**，作用于集合中的每一个的元素

`reduce`是应用于`functools`模块下的，必须先引入`functools`后才可以使用

![1553136073244](.\images\1553136073244.png)

```python
import functools
ret = functools.reduce(lambda x,y:x+y,[1,2,3,4,5])
print(ret)
```



`filter`

![1553137546889](.\images\1553137546889.png)

将集合中的每一个元素传入到函数中**进行过滤**，只会留下符合规则的元素，形成一个列表

```python
ret = filter(lambda x:x<3,[5,1,2,4,6,2])
print(list(ret))
```





**切片**

切片中的[0:4]表示取到第4个为止

```python
names =  ['alex','mary','bob','eric','auto']
print(names[0:4])

# 通过切片去除字符串前后的空格
def trim(text):
    if text[:1] == ' ':
        text = text[1:-1]
    if text[:-1] == ' ':
        text = text[0:-2]
    print(text)

trim(' hello ')
```





**列表生成式**

把一个列表生成一个新的列表

```python
# 过滤出列表中大于2的数据
s = [i for i in range(10) if i>2]
print(s)
[3, 4, 5, 6, 7, 8, 9]

# 或将结果进行计算后，生成新的列表
s = [i**2 for i in range(10) if i>2]
print(s)
[9, 16, 25, 36, 49, 64, 81]

# 或者嵌入两个循环，计算两个数的积
s = [i*j for i in range(10) for j in range(5)]
print(s)
[0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0, 2, 4, 6, 8, 0, 3, 6, 9, 12, 0, 4, 8, 12, 16, 0, 5, 10, 15, 20, 0, 6, 12, 18, 24, 0, 7, 14, 21, 28, 0, 8, 16, 24, 32, 0, 9, 18, 27, 36]
```







unittest：单元测试框架

TestSuite：存储用例

TestLoad：加载用例后存储到TestSuite

Assert：断言

TextTestRunner：出具测试报告



要测试的目标类：

```python
class Calc:
    def __init__(self,first_num,second_num):
        self.first_num = first_num
        self.second_num = second_num

    def add(self):
        return self.first_num+self.second_num

    def multi(self):
        return self.first_num*self.second_num
```



```python
# 先引入自己编写的类，也就是要测试的类
import unittest
from calc import Calc

# 继承unittest.TestCase类是用来写用例的
class TestCalcAdd(unittest.TestCase):
	# 一个用例就是一个函数，不能传参，函数名以test开头，否则不会被执行
    # 当鼠标放置在函数上时，只会执行当前函数
    def test_add_int(self):
        res = Calc(1,2).add()
        print('1+2的结果是:',res)
        # 通过继承于父类self.assertEqual()的方法判断两个值是否相等，msg表示报错信息
        self.assertEqual(2,res,msg='运算出错')

    def test_add_two_zero(self):
        print('0+0的结果是:',Calc(0,1).add())

    def test_add_minus(self):
        print('-1+-2的结果是：',Calc(-1,-2).add())

if __name__ == '__main__':
    # 在执行的过程中，用例被执行的顺序被打乱，这是因为是按照函数名的ASCII码的顺序来决定的
    unittest.main()
   
# ...表示用例运行成功，有几个...就表示执行了几条用例，E表示代码错误，F表示其中一条用例执行失败
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
1+2的结果是: 3
-1+-2的结果是： -3
0+0的结果是: 1
```





通过测试套件执行测试用例

```python
import unittest
# 引入编写了测试用例的类
from ... import TestMathMethod

# 存储用例的容器
suite = unittest.TestSuite()

# 加载方式一：
# 如果在测试用例类以外的地方调用测试用例的函数时，必须先实例化测试类，用例类中的用例函数名
suite.addTest(TestMathMethod('test_add'))
# 执行多条时，需要实例化多个测试类
suite.addTest(TestMathMethod('test_add'))

# 加载方式二：
# 通过loader加载测试类，将测试类中的所有测试用例加载到suite测试套件中
loader = unittest.TestLoader()

# 通过加载测试类
suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))

# 通过加载模块py文件
from xxxx import class_01
suite.addTest(loader.loadTestsFromModule(class_01))

f = open('result.txt','w',encoding = 'utf-8')
# verbosity=2的报告内容更加详细，0、1、2
runner = unittest.TextTestRunner(stream=f, verbosity=2)
runner.run(suite)
```



```python
import HTMLTestRunnerNew

# 保存到html文件中
with open('result.html','wb',encoding='utf-8') as f:
	runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,verbosity=2,title='测试报告',description='描述信息',tester='alex')
runner.run(suite)
```





常用断言方式

assertEqual

assertNotEqual

assertTrue

assertFalse

assertisNone

assertisNotNone

assertin

assertNotin



