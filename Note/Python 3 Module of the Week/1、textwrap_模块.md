textwrap 美 /ræp/ 

**文本执行格式化**模块

```python
#测试文本
sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''
```

#### **fill**:

填充自然段开头

通过fill方法在短文前自动生成了自然段开头，还**可以指定整体文本的位宽**

```python
#textwrap模块,被被翻译为文本换行
import textwrap

print(textwrap.fill(sample_text,width = 50))
#打印得到：通过fill方法在短文前自动生成了自然段开头
'''
     The textwrap module can be used to format
text for output in     situations where pretty-
printing is desired.  It offers     programmatic
functionality similar to the paragraph wrapping
or filling features found in many text editors.
'''
```



#### dedent:

de + indent，去除缩进

使用dedent方法会将每一行紧贴左侧显示，去除缩进

```python
#在使用三引号定义文本时，会有如下的格式，如果使用print打印出来，会原封不动的打印出样式，导致每一段的开头都有空格
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.

import textwrap

#使用dedent方法会将每一行紧贴左侧显示，去除空白
s = textwrap.dedent(sample_text)
print(s)
'''
The textwrap module can be used to format text for output in
situations where pretty-printing is desired.  It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
'''
```



#### fill and dedent:

那么如果使一段文本紧贴左侧，并且可以指定宽度呢，思路是先生成dedent文本，然后将该文本进行fill操作

```python
import textwrap

for width in [45,60]:
    print(f'{width} Columens')
    dedent_text = textwrap.dedent(sample_text).lstrip()
    fill_text = textwrap.fill(dedent_text,width = width)
    print(fill_text)
    print()
'''
45 Columens
The textwrap module can be used to format
text for output in situations where pretty-
printing is desired.  It offers programmatic
functionality similar to the paragraph
wrapping or filling features found in many
text editors.

60 Columens
The textwrap module can be used to format text for output in
situations where pretty-printing is desired.  It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
'''
```



#### **indent:**

/ɪn'dɛnt/行首，在每一行行首添加字符

```python
import textwrap

dedent_text = textwrap.dedent(sample_text)
indent_text = textwrap.indent(dedent_text,'>')
print(indent_text)
'''
>The textwrap module can be used to format text for output in
>situations where pretty-printing is desired.  It offers
>programmatic functionality similar to the paragraph wrapping
>or filling features found in many text editors.
'''
```

还可以根据函数的返回结果，选择是否在行首添加字符

```python
import textwrap

def should_indent(line):
    #{!r}表示将打印的文本连带其附带的所有格式一起打印，其中包含了\n，字符串的符号''等
    print('Indent {!r}'.format(line.strip()))
    #计算每一行的字符数，是否是2的倍数，返回True或False，在textwarp.indent()方法中，predicate参数会根据返回结果，来确定是否添加对应的行首字符，
    return len(line.strip()) % 2 == 0

dedent_text= textwrap.dedent(sample_text)
fill_text = textwrap.fill(dedent_text,width = 50)
#虽然返回结果是True和False，但是不能直接写为True和False，会报错，将指定函数传给predicate参数，接收到文本后，会在源码中循环每一行内容，判断后输出， 美/ˈprɛdɪˌkeɪt/：断言
indent_text = textwrap.indent(fill_text,'EVEN',predicate = should_indent)

print('\nQuoted block')
print(indent_text)
'''
Indent 'The textwrap module can be used to format text'
Indent 'for output in situations where pretty-printing is'
Indent 'desired.  It offers programmatic functionality'
Indent 'similar to the paragraph wrapping or filling'
Indent 'features found in many text editors.'

Quoted block
EVEN The textwrap module can be used to format text
for output in situations where pretty-printing is
EVENdesired.  It offers programmatic functionality
EVENsimilar to the paragraph wrapping or filling
EVENfeatures found in many text editors.
'''
```



#### initial_indent&subsequent_indent

隶属于fill方法中的参数

```python
import textwrap

dedent_text = textwrap.dedent(sample_text)
fill_text = textwrap.fill(dedent_text.strip(),
                          # /ɪ'nɪʃəl/ 在最初的首行添加字符
                          initial_indent = 'a', 
                          # /'sʌbsɪkwənt/，在随后的每行行首添加字符
                          subsequent_indent = ' ' * 4, 
                          width = 50)
print(fill_text)
'''
aThe textwrap module can be used to format text
    for output in situations where pretty-printing
    is desired.  It offers programmatic
    functionality similar to the paragraph
    wrapping or filling features found in many
    text editors.
'''
```



#### shorten:

将一整段文字，根据指定的字符宽度，缩略为一小段

```python
import textwrap

dedent_text = textwrap.dedent(sample_text)
fill_text = textwrap.fill(dedent_text,width = 50)

#shorten 美 /'ʃɔrtn/ 缩短
shorten_text = textwrap.shorten(fill_text,50)
print(shorten_text)
'''
The textwrap module can be used to format [...]
'''
```

