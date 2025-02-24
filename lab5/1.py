import re
a=input().strip()
p=r'ab*'
res=bool(re.fullmatch(p,a))
print(res)