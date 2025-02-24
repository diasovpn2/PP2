import re
def c (s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower() 
a = input()
b = c (a) 
print(b)
