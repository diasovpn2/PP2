from lab10a.phone.db import connect

conn = connect()
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        phone VARCHAR(15)
    );
""")

conn.commit()
cur.close()
conn.close()

print("Таблица создана!")
