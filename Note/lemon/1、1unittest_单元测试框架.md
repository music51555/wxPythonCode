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



**通过`unittest`类编写测试用例**

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





**通过测试套件执行测试用例**

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



**`setUp`和`tearDown`**

继承于`unittest.TestCase`夹心饼干

在每一条用例执行前都会执行`setUp`，初始化测试环境

在每一条用例执行后都会执行`tearDown`，清理测试环境

如在每一条测试用例前都要执行xxx的打开操作，或关闭操作时使用

```python
import unittest
from requests_pack.http_request import HttpRequest

class KTPLoginTestCase(unittest.TestCase):
    def setUp(self):
        print('准备开始执行用例')

    def test_right_username_and_password(self):
        login_res = HttpRequest('18611848257','nishi458')\
            .request_post().json()
        self.assertEqual('success',login_res['info'])

    def test_right_username_and_error_password(self):
        login_res = HttpRequest('18611848257','nishi4581')\
            .request_post().json()
        self.assertEqual('success',login_res['info'])

    def tearDown(self):
        print('当前测试用例执行完毕')

if __name__ == '__main__':
    unittest.main()
    
准备开始执行用例
当前测试用例执行完毕
准备开始执行用例
当前测试用例执行完毕
```



**在测试用例中初始化属性，供每一条测试用例执行**

```python
class LoginTestCase(unittest.TestCase):
    # 继承了TestCase类后，可以在类中调用__init__方法初始化属性，但是父类的super__init__()方法也必须必不可少，因为要传入测试用例的方法名
    def __init__(self,methodName,url,data,cookie,expect):
        super().__init__(methodName)
        self.url = url
        self.data = data
        self.cookie = cookie
        self.expect = expect

    def test_right_u_right_p(self):
        response = HTTPRequest(url=self.url,data=self.data).request_post()
        if response.cookies:
            setattr(get_cookies.GetCookies,'cookies',response.cookies)
        self.assertEqual(self.expect,re.search('登录成功',response.text).group())

    def test_right_u_error_p(self):

        response = HTTPRequest(url=self.url,data=self.data).request_post()
        self.assertEqual(self.expect,re.search('帐号或密码错误!',response.text).group())

    def test_empty_u_have_p(self):

        response = HTTPRequest(url=self.url,data=self.data).request_post()
        self.assertEqual(self.expect,re.search('此账号没有经过授权，请联系管理员!',response.text).group())
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



