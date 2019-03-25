**ddt**

`ddt`模块的作用是向继承于`unittest.TestCase`类中的测试用例传递参数



**`@ddt`装饰器**

**`@ddt`装饰器必须添加在测试用例的类之上，且类必须继承于`unittest.TestCase`**

`pip3 install ddt`

```
from ddt import ddt,data,unpack
```



**`@data`装饰器**

**`@data`装饰器的作用是脱掉传递参数的外套，逐一接收列表内的每一个元素，但是必须添加"*"**

1、测试类必须添加`@ddt`装饰器

2、如果要传递参数，测试用例函数必须添加`@data`

3、如果要原封不动传递参数，直接写对应的参数名

4、如果使用非固定参数接收` @data(*num_list)`，那么**接收几个元素，测试用例就会被执行几次**

```python
import unittest
from ddt import ddt,data,unpack


num_list = [[3,4],[1,2],[5,6]]

@ddt
class TestDDT(unittest.TestCase):

    @data(*num_list)
    def test_data(self,num):
        print('%s\n'%num)


if __name__ == '__main__':
    unittest.main()

# 得到的结果是：
[3, 4]
[1, 2]
[5, 6]
```



**如果列表中存放的是字典数据**

**得到的结果也是列表中的每一个字典，有几个字典测试用例就会被执行几次**

```python
name_list = [{'name':'alex','sex':'male'},{'name':'mary','sex':'female'}]

@ddt
class TestDDT(unittest.TestCase):

    @data(*name_list)
    def test_data(self,info):
        print('%s\n'%info)

if __name__ == '__main__':
    unittest.main()
    
# 得到的结果是：
{'name': 'alex', 'sex': 'male'}
{'name': 'mary', 'sex': 'female'}
```





**`@unpack`装饰器**

**`@unpack`装饰器的作用是：在`@data`脱掉最外层外套后，将列表中的其一元素继续拆包为单个元素，且测试用例函数接收的参数必须与列表中元素的个数匹配**

```python
import unittest
from ddt import ddt,data,unpack


num_list = [[1,2],[3,4],[5,6]]

@ddt
class TestDDT(unittest.TestCase):

    @data(*num_list)
    @unpack
    def test_data(self,num1,num2):
        print('%s,%s\n'%(num1,num2))

if __name__ == '__main__':
    unittest.main()

# 得到的结果是：
1,2
3,4
5,6
```



**如果列表中存放的是字典数据**

脱掉外套后，列表中的元素如果是字典，那么测试用例接收的参数是每一个字典的`key`值，有几个字典就被执行几次，分别打印出每一个字典的`value`值

```python
import unittest
from ddt import ddt,data,unpack


name_list = [{'name':'alex','sex':'male'},{'name':'mary','sex':'female'}]

@ddt
class TestDDT(unittest.TestCase):

    @data(*name_list)
    @unpack
    def test_data(self,name,sex):
        print('%s\n'%name)
        print('%s\n'%sex)

if __name__ == '__main__':
    unittest.main()

# 得到的结果是：
alex
male
mary
female
```





**`ddt`和`unittest`结合使用**

如果是依次将测试数据传入测试用例中，那么只需要写一个登录的测试用例即可，因为有多少条测试数据，就会执行多少次测试用例，且传入的测试数据是不同的

```python
# 引入DoExcel类执行get_case_list方法得到所有的测试用例数据
case_list = DoExcel('util/testcase_data.xlsx', 'login').get_case_list()

# 在测试用例类上添加ddt装饰器
@ddt
class LoginTestCase(unittest.TestCase):

    login_url = 'http://120.78.128.25:8765/Frontend/Index/login'

    def setUp(self):
        print('开始测试')

    # 在测试用例方法上添加@data装饰器，接收参数
    @data(*case_list)
    def test_login_api(self,testcase):
        response = HTTPRequest(url=self.login_url,data=eval(testcase['case_data'])).request_post()
        if response.cookies:
            setattr(get_cookies.GetCookies,'cookies',response.cookies)
        try:
            really = re.search(testcase['case_expected'],response.text).group()
        except AttributeError as e:
            # 如果程序捕获了异常，那么就打印当前用例的方法名，并报出异常，用于在测试报告中查看输出日志
            print(testcase['case_desc'])
            raise e
        else:
            self.assertEqual(testcase['case_expected'],really)
```

