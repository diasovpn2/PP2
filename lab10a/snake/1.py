from db import connect
con=connect()
cur=con.cursor()
cur.execute("SELECT * FROM snake")
r=cur.fetchall()
for i in r:
    print(i)
cur.close()
con.close()