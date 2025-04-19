from lab10a.phone.db import connect

conn = connect()
cur = conn.cursor()

name = input("Введите имя пользователя для удаления: ")

try:
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    conn.commit()
    print("Пользователь успешно удалён.")
except Exception as e:
    print("Ошибка при удалении:", e)
finally:
    cur.close()
    conn.close()
