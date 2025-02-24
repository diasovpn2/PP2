import re 
a=input().strip()
p=r'[A-Z][a-z]+'
print(bool(re.fullmatch(p,a)))