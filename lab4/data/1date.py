from datetime import datetime,timedelta
d=datetime.today()
m=d-timedelta(days=5)
print(d.strftime("%Y-%m-%d"))
print(m.strftime("%Y-%m-%d"))