通过`pandas`读取`excel`文档

创建实例名称为`df`，表示为`dataframe`，数据框架



##### 创建`Excel`文件对象

```python
excel_file = pandas.ExcelFile('test_case.xlsx')
print(excel_file.parse('login').ix[1].to_dict())
print(excel_file.sheet_names)
```



##### 创建工作簿对象

```python
wb = pandas.read_excel('test_case.xlsx','register')
```



```python
import pandas

# 通过read_excel(文件名称，工作簿名称)创建所有的工作簿对象wb
wb = pandas.read_excel('test_case.xlsx','register')

# 直接打印wb得到的是矩阵的列表
print(wb)

   case_id      case_title  ... case_expected  result
0        1    正确手机号和正确密码注册  ...         10001   20110
1        2     输入已注册的手机号注册  ...         20110   20110
2        3    输入错误格式的手机号注册  ...         20109   20109
3        4       输入不足6位的密码  ...         20108   20110
4        5  不输入用户名，不输入密码注册  ...         20103   20103


# 打印wb.value将每一行的数据放入列表中，并将所有行的数据也依次放入列表中
print(wb.values)

[
  [1 '正确手机号和正确密码注册'
  "{'mobilephone':'18611848257','pwd':'nishi458','regname':'乐乐'}" 10001
  20110]
 [2 '输入已注册的手机号注册'
  "{'mobilephone':'18611848257','pwd':'nishi458','regname':'乐乐'}" 20110
  20110]
 [3 '输入错误格式的手机号注册'
  "{'mobilephone':'1861184825','pwd':'nishi458','regname':'乐乐'}" 20109
  20109]
 [4 '输入不足6位的密码'
  "{'mobilephone':'13810504359','pwd':'123456','regname':'乐乐'}" 20108
  20110]
 [5 '不输入用户名，不输入密码注册' "{'mobilephone':'','pwd':'','regname':'乐乐'}" 20103
  20103]
]


# 通过wb.ix按行索引打印第一行的数据的矩阵样式
print(wb.ix[0])
case_id                                                          1
case_title                                            正确手机号和正确密码注册
case_data        {'mobilephone':'18611848257','pwd':'nishi458',...
case_expected                                                10001
result                                                       20110
Name: 0, dtype: object
           
# 按索引打印第0行的第2个单元格中的内容
print(wb.ix[0,2])
正确手机号和正确密码注册


# 对第一行数据添加values，是按列表存储第一行数据
print(wb.ix[0].values)
[1 '正确手机号和正确密码注册'
 "{'mobilephone':'18611848257','pwd':'nishi458','regname':'乐乐'}" 10001
 20110]

# 对一行数据调用to_dict()方法，将第一行数据存储在字典中
print(wb.ix[0].to_dict())
{'case_id': 1, 'case_title': '正确手机号和正确密码注册', 'case_data': "{'mobilephone':'18611848257','pwd':'nishi458','regname':'乐乐'}", 'case_expected': 10001, 'result': 20110}


# 同样还支持切片操作，意思是打印当前工作薄从索引0行打印至索引2行
print(wb.ix[:2])

                     
# 打印当前工作簿所有行的索引，不包含标题行
print(wb.index.values)
[0 1 2 3 4]
   
                  
# 随机抽取数量的测试用例
print(wb.sample(3).values)

for i in wb.sample(3).values:
    print(wb.ix[i[0]-1].to_dict())
{'case_id': 3, 'case_title': '输入错误格式的手机号注册', 'case_data': "{'mobilephone':'1861184825','pwd':'nishi458','regname':'乐乐'}", 'case_expected': 20109, 'result': 20109}
                  
{'case_id': 2, 'case_title': '输入已注册的手机号注册', 'case_data': "{'mobilephone':'18611848257','pwd':'nishi458','regname':'乐乐'}", 'case_expected': 20110, 'result': 20110}
                  
{'case_id': 5, 'case_title': '不输入用户名，不输入密码注册', 'case_data': "{'mobilephone':'','pwd':'','regname':'乐乐'}", 'case_expected': 20103, 'result': 20103}
```





##### 方法总结：

通过`pandas.read_excel(文件名，工作簿名)`创建`wb`对象

`print(wb)`直接打印`wb`对象，得到的是矩阵式的表格式的数据，不常用

`print(wb.values)`将每一行的数据值都放在列表中，并将所有行也都放在列表中，不常用

`print(wb.ix[1].values)`通过`wb`对象的`ix`方法指定行号输出这一行的数据，在列表中，不常用

`print(wb.ix[1].to_dict())`通过`wb`对象的ix方法指定行号输出这一行的数据，在字典中，常用

`print(wb.ix[1,1])`按行和列的索引取出单元格内的值，用来取值，常用

`print(wb.index.values)`在列表中输出所有行号的索引`[0,1,2,3...]`，可以用来循环每一行

`print(wb.sample(2).values)`随机取出`n`条用例，数据和测试用例都存储在列表中



**常用方法配合总结：**

##### 1、循环`wb.index.values`索引列表，创建所有行的测试数据

```pythoN
case_list = []

for index in wb.index.values:
    case = wb.ix[index].to_dict()
    case_list.append(case)

print(case_list)
[
{'case_id': 1, 'case_title': '正确手机号和正确密码注册', 'case_data': "{'mobilephone':'18611848257','pwd':'nishi458','regname':'乐乐'}", 'case_expected': 10001, 'result': 20110}, 
{'case_id': 2, 'case_title': '输入已注册的手机号注册', 'case_data': "{'mobilephone':'18611848257','pwd':'nishi458','regname':'乐乐'}", 'case_expected': 20110, 'result': 20110}, 
{'case_id': 3, 'case_title': '输入错误格式的手机号注册', 'case_data': "{'mobilephone':'1861184825','pwd':'nishi458','regname':'乐乐'}", 'case_expected': 20109, 'result': 20109}, 
{'case_id': 4, 'case_title': '输入不足6位的密码', 'case_data': "{'mobilephone':'13810504359','pwd':'123456','regname':'乐乐'}", 'case_expected': 20108, 'result': 20110}, 
{'case_id': 5, 'case_title': '不输入用户名，不输入密码注册', 'case_data': "{'mobilephone':'','pwd':'','regname':'乐乐'}", 'case_expected': 20103, 'result': 20103}
]
```



##### 2、循环指定索引，创建某些行的测试数据

```pythoN
case_list = []

# 实现从配置文件中读取要执行测试用例的序号，来创建测试数据列表
for index in [1,2,4]:
    case = wb.ix[index].to_dict()
    case_list.append(case)

print(case_list)
```



##### 3、随机选择n条的测试用例，进行测试

```pythoN
# wb.sample(n).values是随机抽取n条测试用例，都存放在列表中
random_case_list = wb.sample(2).values
case_list = []

# 循环存放测试用例的列表，并通过wb.ix[n]取出每一条用例[0]位置的序号，来取出这一行测试数据，在字典中
for r_case in random_case_list:
    case = wb.ix[r_case[0]-1].to_dict()
    case_list.append(case)

print(case_list)
```



##### 将内容写入到其他类型的文件中，支持`excel、json、html`等

将读取出的内容，在创建`pands.ExcelWriter(file_name) as file`来实现将输入写入到新的`excel`中

```python
df = pandas.read_excel('test_case.xlsx','register')

with pandas.ExcelWriter('new.xlsx') as file:
    df.to_excel(file,'test')
```

