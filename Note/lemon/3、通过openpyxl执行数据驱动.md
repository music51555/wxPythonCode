通过`openpyxl`执行数据驱动

实现方式：

循环excel中的每一行时，都会新建一个字典，通过`login_sheet(row,1).value`、`login_sheet(row,2).value`....获取每一列的值，赋值到字典的`testcase['method_name']`...中，最后将每一行数据的字典添加到列表中

```python
from openpyxl import load_workbook

def get_value():
    # 通过读取xlsx文件，获取所有的工作薄对象
    wb = load_workbook('util/testcase_data.xlsx')
    
    # 通过字典获取其中的工作薄对象
    login_sheet = wb['login']
    testcase_list = []
    
    # max_row和max_column表示最大行数和最大列数
    for row in range(1,login_sheet.max_row+1):
        testcase = {}

        testcase['method_name'] = login_sheet.cell(row,1).value
        testcase['data'] = login_sheet.cell(row,2).value
        testcase['expect'] = login_sheet.cell(row,3).value

        testcase_list.append(testcase)

    return testcase_list
```





第二种方法是，先循环第一行的每一列，得到每一列的title，如**用例编号**、**用例描述**等，放置在列表中，用于在循环测试数据的每一行时创建一个字典，并在循环每一列时，用列表中的用例编号、用例描述作为字典的key，来把每一列的数据放置在字典中

```python
class DoExcel:
    def __init__(self,file_name,sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name
        self.login_sheet = load_workbook(file_name)[sheet_name]

    def get_header(self):
        header_list = []
        for column in range(1,self.login_sheet.max_column+1):
            header_list.append(self.login_sheet.cell(1,column).value)
        return header_list

    def get_value(self):
        header_list = self.get_header()
        case_list = []
        for row in range(2,self.login_sheet.max_row+1):
            test_case = {}
            for column in range(1,self.login_sheet.max_column+1):
                test_case[header_list[column-1]] = self.login_sheet.cell(row,column).value
            case_list.append(test_case)
        return case_list
```

展示最后返回的数据

```json
[
    {
        '用例编号': 1,
        '用例描述': '正确的用户名和密码',
        '用例名称': 'test_right_u_right_p',
        '测试数据': "{'phone':'18611848257','password':'nishi458','vcode':'','remember_me':'1','notify_url':''}",
        '预期结果': '登录成功'
    },
    {
        '用例编号': 2,
        '用例描述': '正确的用户名和错误的密码',
        '用例名称': 'test_right_u_error_p',
        '测试数据': "{'phone':'18611848257','password':'nishi459','vcode':'','remember_me':'1','notify_url':''}",
        '预期结果': '帐号或密码错误!'
    },
    {
        '用例编号': 3,
        '用例描述': '只输入用户名不输入密码',
        '用例名称': 'test_empty_u_have_p',
        '测试数据': "{'phone':'','password':'nishi458','vcode':'','remember_me':'1','notify_url':''}",
        '预期结果': '此账号没有经过授权，请联系管理员!'
    }
]
```







**re.sub的使用方法**

在excel中读取的数据，整型是整型，浮点型是浮点型，但其他读取出来的都是字符串，如字典类型

```python
# 读取出来的字符串如果通过json.loads读取数据，会报错，因为json数据中的key没有使用双引号括起来，所以需要使用re来实现替换为双引号的效果
s = '{'name':'alex','sex':'male'}'
re.sub("\'",'\"'.s)
```



通过`re.sub(旧数据，新数据，目标字符串)`来实现替换数据

因为`str.replace(旧数据，新数据)`只能替换固定的旧数据，而`re.sub`能通过`\d+`等匹配数据后替换

```python
import re

s = 'hello 100 world 120'
re.sub('\d+','cat',s)
将被替换为'hello cat world cat'
```



**但提供更简便的方法`eval`**

将读取出来的字符串数据直接转换为对应的数据类型

```python
s = '{'name':'alex','sex':'male'}'
# 直接将eval变为字典类型
eval(s)
```



**将数据回写到Excel中**

```python
def set_value(self):
    # 可以通过sheet.cell(row.column).value取到值
    # 也可以通过sheet.cell(row,column).value = xxxxx来写入值
    self.sheet.cell(self.kwargs['row']+1,5).value = self.kwargs['value']
    
    # 最后通过wb对象调用save()方法回写到excel中
    self.wb.save(self.file_name)
```





excel中写上title，循环得到每一行的值，根据每一行的值去创建字典，e



















