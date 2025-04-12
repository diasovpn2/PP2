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
for row in rows:
    print(f"ID: {row[0]} | Name: {row[1]} | Phone number: {row[2]}")

choice = int(input("Which contact u want to delete?: '1 - phone', '2 - name' "))
if choice == 1:
    phone = input("Enter the phone: ")
    cur.execute(
        "DELETE FROM Phonebook WHERE phone LIKE %s", (f'{phone}',)
    )
    print("The contact deleted")
elif choice == 2:
    name = input("Enter the name: ")
    cur.execute(
        "DELETE FROM Phonebook WHERE name LIKE %s", (f'{name}',)
    )
    print("The contact deleted")
else:
    print("Error")
conn.commit()
print("          NEW CONTACTS")
cur.execute("SELECT * FROM Phonebook")
rows = cur.fetchall()
for row in rows:
    print(f"ID: {row[0]} | Name: {row[1]} | Phone number: {row[2]}")
cur.close()
conn.close() 