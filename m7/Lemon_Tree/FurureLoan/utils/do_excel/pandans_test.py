import pandas

df = pandas.read_excel('test_case.xlsx','register')

with pandas.ExcelWriter('new.xlsx') as file:
    df.to_excel(file,'test')
