import psycopg2
conn = psycopg2.connect(
    host = "localhost",
    dbname = "phonebook_db",
    user = "postgres",
    password = "qazplm123"
)
cur = conn.cursor()
cur.execute("SELECT * FROM Phonebook")
rows = cur.fetchall()
print()
for row in rows:
    print(f"ID: {row[0]} | Name: {row[1]} | Phone number: {row[2]}")