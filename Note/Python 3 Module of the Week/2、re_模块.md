```python
import re

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern,text)

#s和e表示匹配到内容的开始和结束索引
s = match.start()
e = match.end()

#match.string表示要匹配的内容
print( f'in "{match.string}"\n'
       #match.re.pattern表示匹配到数据
       f'Found {match.re.pattern}\n'
       f'from {s} to {e} ("{text[s:e]}")')

'''
in "Does this text match the pattern?"
Found this
from 5 to 9 ("this")
'''
```

