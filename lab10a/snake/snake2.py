import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Qazmlp12"
    )

# Подключаемся к базе данных
conn = connect()
cur = conn.cursor()

# Таблица user
cur.execute("""
CREATE TABLE IF NOT EXISTS "user" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE
)
""")

# Таблица user_score
cur.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES "user"(id),
    score INTEGER,
    level INTEGER,  -- Исправлено с NUMBER на INTEGER
    date_played TIMESTAMP DEFAULT current_timestamp
)
""")

# Подтверждаем изменения и закрываем соединение
conn.commit()
cur.close()
conn.close()

print("Tables created!")
