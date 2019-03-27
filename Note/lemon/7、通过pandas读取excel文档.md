通过pandas读取excel文档

```python
import pandas

# 默认读取第一个工作薄数据，指定sheet_name后读取对应工作薄的数据
wb = pandas.read_excel(file_name,sheet_name)
wb.values
# 默认不包含title行，索引从0开始
wb.index.values
wb.ix[1].to_dict()
wb.ix[行号，列号]
wb.ix[:]
wb.ix[:['url']]
wb.ix[:['url','data']]
wb.ix[1].values

```



ddt或超继承

写入excel

同时运行多个测试用例集里面的多条测试用例

