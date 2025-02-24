import re 
a=input().strip()
p=re.sub(r"[ ,.]",":",a)
print(p)