from lab10a.phone.db import connect

conn = connect()
cur = conn.cursor()
cur.execute("SELECT * FROM phonebook WHERE phone LIKE '+7%'")
results = cur.fetchall()
if results: 
    print("Есть номера на +7. Примеры:")
    for row in results[:3]:
        print(row)
else:
    print("Нет номеров на +7")
cur.close()
conn.close()