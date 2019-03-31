##### 更新`Excel`单元格内的值

在接口参数的单元格内，手机号总是会需要更新为一个未使用的手机号，如果不更新，将会重复使用这一个手机号，所以将`excel`中的内容设置为

![1553847118436](.\1553847118436.png)



在程序中通过`pandas`获取单元格的数据后，将其通过`find`查找，`resplace`替换为新的手机号

```python
# 手机号做了+1操作
if case_info['case_data'].find('$(tel)')!=-1:
	case_info['case_data'] = case_info['case_data'].replace('$(tel)',str(init_tel))
```



`pandas`的`to_excel`方法在打开文件后，是根据当前传入的文件名和工作薄，去保存为`excel`文件的，在循环每一个工作薄的名称时，`df`对象内存储的总是最后一个工作薄的内容，所以还是推荐使用`openpyxl`的模块

```python
def update_tel(self,sheet_name,new_tel):
	sheet = self.wb[sheet_name]
	sheet.cell(2,2).value = new_tel+1
	self.wb.save(self.file_name)
```





针对于有`if…elif…elif…else`的情况下，如果在判断过程中支持2种判断，不要写在一个判断下，否则在一个判断满足的情况下，不会去执行另一个判断下的内容，都写为`if…if...`

```python
    def replace_data(self,case_info,sheet_name):
        if case_info['case_data'].find('${tel}') != -1:
            self.init_tel = int(pandas.read_excel(self.file_name, 'init').ix[0, 1]) + 1
            case_info['case_data'] = case_info['case_data'].replace('$(tel)', str(self.init_tel))
        if case_info['case_data'].find('${admin_tel}') != -1:
            self.admin_tel = int(pandas.read_excel(self.file_name, 'init').ix[1, 1])
            case_info['case_data'] = case_info['case_data'].replace('${admin_tel}', str(self.admin_tel))
        if case_info['case_data'].find('${invest_memid}') != -1:
            self.invest_memid = int(pandas.read_excel(self.file_name, 'init').ix[3, 1])
            case_info['case_data'] = case_info['case_data'].replace('${invest_memid}', str(self.invest_memid))
        if case_info['case_data'].find('${loan_id}')!=-1:
            loan_id = self.get_loanid()
            case_info['case_data'] = case_info['case_data'].replace('${loan_id}', str(loan_id))
        case_info['sheet_name'] = sheet_name
```

