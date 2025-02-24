import re
a=input().strip()
f=r'.*a.*b$'
print(bool(re.fullmatch(f,a)))