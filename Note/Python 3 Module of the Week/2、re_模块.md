#### **search**

文本查找模式

search函数扫描文本，如果找到匹配文本，则会返回文本，如果没有找到返回None

```python
import re

pattern_text = 'this'
text = 'Does this text match the pattern?'

#通过search查找指定文本，start()和end()表示结果文本的开始和结束索引
r = re.search(pattern_text,text)
s = r.start()
e = r.end()
print('find %s start %s,end %s'%(r.group(),s,e))

#如果没有找到指定文本，则会报错，说明返回的是个None
AttributeError: 'NoneType' object has no attribute 'group'
```



#### compile

compile   美 /kəm'paɪl/

编译一个正则表达式对象，通过对象匹配更快速，优点是在程序启动时，就已经编译好了正则表达式

```python
import re

r = re.compile('\w+@\w+.(com|net|cn)')
s = bool(r.search('lelevipforever@sina.com'))
print(s)
'''
True
'''
```



#### findall

查找所有匹配到的数据，**返回一个列表**

```python
import re

r = re.findall('ab','abbaaabbbbaaaaa')
print(r)
'''
['ab', 'ab']
'''
```



#### finditer

查找所有匹配的数据，**返回一个迭代器**

```python
import re

patter = 'ab'
text = 'abbaaabbbbaaaaa'
r = re.finditer(patter,text)
print(r)

for match in r:
    s = match.start()
    e = match.end()

    print(text[s:e])
'''
<callable_iterator object at 0x00000000021DC438>
ab
ab
'''
```



**以下方法中的特殊符号，作用于紧挨着的字符**

#### *0次或多次

```python
import re

#其中*表示字符集中的字符可以出现0次或多次,0次表示可以不出现，以先匹配到的为准
r = re.search('ab*','a followed by zero or more a')
print(r.group())
'''
a
'''
```



#### +至少要出现1次或多次

```python
import re

#其中+表示字符集中的b字符至少要出现1次或多次,而不是只ab字符，以先匹配到的为准
r = re.search('ab+','a followed by abbzero or more abz')
print(r.group())
'''
abb
'''
```



#### ?0次或1次

```python
import re

#其中?表示b可以匹配0次或1次，0次表示不出现,以先匹配到的为准
r = re.search('ab?','ac followed by abbzero or more abz')
print(r.group())
'''
a
'''
```



**{}**

```python
import re

#其中{}表示匹配b，3次，以先匹配到的为准
r = re.search('ab{3}','c followed by bbzero or more abbb')
print(r.group())
'''
abbb
'''
```



**{m,n}**

```python
import re

#其中{m,n}表示匹配2次或3次b，m是最小重复数，n是最大重复数,以先匹配到的为准
r = re.search('ab{2,3}','c followed by bbzero or more abb')
print(r.group())
'''
abb
'''
```



**[]**

```python
import re

#其中[]表示可以匹配字符集中的任一字符，以先匹配到的为准
r = re.search('ab[ab]','c followed by bbzero or more aba')
print(r.group())
'''
aba
'''
```



**[^ ]**

```python
import re

#其中[^ ]表示不匹配字符集中的任一字符，排除字符集中的字符，以先匹配到的为准
r = re.search('ab[^ab]','c followed by bbzero or more abz')
print(r.group())
'''
abz
'''
```



**^**

```python
import re

#其中^表示匹配整段文字的开头，检查是否以ab1开头
r = re.search('^ab1','ab1 c followed by bbzero or more ')
print(r.group())
'''
ab1
'''
```



**[a-z]**

```python
import re

#其中[a-z]表示可以匹配a-z中的任一个，0次或多次,以先匹配到的为准
r = re.search('a[a-z]','ab1 c followed by bbzero or more ')
print(r.group())
```



**[a-zA-Z]**

```python
import re

#其中**[a-zA-Z]**表示合并查找a-z和A-Z的字符集,以先匹配到的为准
r = re.search('a[a-zA-Z]{3}','ab1 c followed by bbzero or more abcde')
print(r.group())
```



**.**

```python
import re

#其中.表示可以匹配任意字符
r = re.search('a.','ab1 c followed by bbzero or more abcde')
print(r.group())
```



**转移符：**

**\d**

a digit

```python
import re

#其中\d表示一个数字,以先匹配到的为准
r = re.search('a\d','ab1 c followed by bbzero or more a3')
print(r.group())
'''
a3
'''
```



**\D**

non digit

```python
import re

#其中*表示可以匹配pattern字符中的任一字符，0次或多次,以先匹配到的为准
r = re.search('a\D','ab1 c followed by bbzero or more a3')
print(r.group())
'''
ab
'''
```



**\\s**

表示匹配空白符

```python
import re

#其中\s表示可以匹配tab, space, newline, etc等
r = re.search('a\s','a  b1 c followed by bbzero or more a3')
print(r.group())
'''
a 
'''
```



**\S**

表示匹配非空白符

```python
import re

#其中\S表示可以匹配非空白字符,以先匹配到的为准
r = re.search('a\S','a  b1 c followed by bbzero or more a3')
print(r.group())
'''
a3
'''
```



**\w**

```python
import re

#其中\w表示可以匹配字母或数字
r = re.search('a\w','a  b1 c followed by bbzero or more a3')
print(r.group())
'''
a3
'''
```



**\W**

```python
import re

#其中\W*表示可以匹配非字母和数字
r = re.search('a\W','a!  b1 c followed by bbzero or more a3')
print(r.group())
'''
a!
'''
```



**r**

如果是“\n”那么表示一个反斜杠字符，一个字母n，而不是表示换行了 

```python
import re

#其中r表示使字符串中的转移符默认变为不转义
#如\d表示一个数字，但是添加r后，就变为普通的\和d两个字符了
r = re.search(r'a\\d+','a\dd  b1 c followed by bbzero or more a3')
print(r.group())
print(r'\asd')
'''
\asd
'''
```