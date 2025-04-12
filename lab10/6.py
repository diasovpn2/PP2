import psycopg2
conn = psycopg2.connect(
    host = "localhost",
    dbname = "phonebook_db",
    user = "postgres",
    password = "qazplm123"
)
cur = conn.cursor()
what = int(input("Searching by name(1) or by phone(2): "))
if what == 1:
    name = input("Enter the name: ")
    cur.execute(
        "SELECT * FROM Phonebook WHERE name LIKE %s", (f"%{name}%",)
    )
    rows = cur.fetchall()
    for row in rows:
        print(f'ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}')
elif what == 2:
    phone = input("Enter the phone: ")
    cur.execute(
        "SELECT * FROM Phonebook WHERE phone LIKE %s", (f"%{phone}%",)
    )
    rows = cur.fetchall()
    for row in rows:
        print(f'ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}')
conn.commit()
cur.close()
conn.close()