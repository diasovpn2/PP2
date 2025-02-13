from datetime import datetime
a=datetime(2005,11,11,20,21,10)
b=datetime(2005,11,11,20,22,10)
d=abs((b-a).total_seconds())
print(d)