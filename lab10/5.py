import psycopg2
# Подключаемся к базе данных
conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook_db",
    user="postgres",
    password="qazplm123"
)
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS Phonebook(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    phone VARCHAR(20)
)            
            ''')
conn.commit()
cur.close()
conn.close()
print("well done")