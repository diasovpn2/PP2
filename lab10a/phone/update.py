import psycopg2
from db import connect

conn = connect()
cur = conn.cursor()

name = input("Введите имя пользователя, которого нужно обновить: ")
new_phone = input("Введите новый номер телефона: ")

try:
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    print("Номер успешно обновлен.")
except Exception as e:
    print("Ошибка при обновлении:", e)
finally:
    cur.close()
    conn.close()
