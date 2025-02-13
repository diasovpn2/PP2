from datetime import datetime,timedelta
a=datetime.today()
b=a-timedelta(days=1)
c=a+timedelta(days=1)
print("сегодня",a.strftime("%Y-%m-%d"))
print("вчера",b.strftime("%Y-%m-%d"))
print("завтра",c.strftime("%Y-%m-%d"))