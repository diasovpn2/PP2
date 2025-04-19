from db import connect

conn = connect()
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        phone VARCHAR(11)
    );
""")

conn.commit()
cur.close()
conn.close()

print("Таблица создана!")
