import re

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern,text)

s = match.start()
e = match.end()

print( f'in "{match.string}"\n'
       f'Found {match.re.pattern}\n'
       f'from {s} to {e} ("{text[s:e]}")')