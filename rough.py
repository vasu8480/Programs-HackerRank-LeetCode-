import re

p=re.compile("[A-Z][a-z]+")
a=(p.match("Hello World"))
print(a.group())