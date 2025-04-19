from lab10a.phone.db import connect

conn = connect()
cur = conn.cursor()

filter_name = input("Введите имя для поиска: ")

cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", ('%' + filter_name + '%',))
results = cur.fetchall()

if results:
    print("Результаты поиска:")
    for row in results:
        print(row)
else:
    print("Ничего не найдено.")

cur.close()
conn.close()
