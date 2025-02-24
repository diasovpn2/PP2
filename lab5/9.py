import re
a=input()
r=re.sub(r"([a-z])([A-Z])",r"\1 \2",a)
print(r)