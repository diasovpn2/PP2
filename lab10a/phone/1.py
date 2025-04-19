from lab10a.phone.db import connect

conn = connect()
cur = conn.cursor()

cur.execute("SELECT * FROM phonebook")
rows = cur.fetchall()

print("Текущее содержимое таблицы phonebook:")
for row in rows:
    print(row)

cur.close()
conn.close()
