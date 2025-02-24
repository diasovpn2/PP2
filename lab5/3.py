import re 
a=input().strip()
p=r'[a-z]+(?:_[a-z]+)*'
res=bool(re.fullmatch(p,a))
print(res)