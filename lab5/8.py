import re
a=input()
def r(a):
    return " ".join(re.findall(r'[A-Z][a-z]*',a))
print(r(a))