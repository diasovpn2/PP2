import re
a=input().strip()
p=r'ab{2,3}'
s=bool(re.fullmatch(p,a))
print(s)