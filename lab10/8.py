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
choice = int(input("What do u want to change?: '1 - name', '2 - phone' "))
if choice == 1:
    phone = input("Enter the phone: ")
    new_name = input("Enter new name: ")
    cur.execute(
        "Update Phonebook SET name = %s WHERE phone = %s", (new_name, phone)
    )
    print("The contact updated")
elif choice == 2:
    name = input("Enter the name: ")
    new_phone = input("Enter new phone: ")
    cur.execute(
        "Update Phonebook SET phone = %s WHERE name = %s", (new_phone, name)
    )
    print("The contact updated")
else:
    print("Error")
conn.commit() 
print("           New Phonebook ")
cur.execute("SELECT * FROM Phonebook")
rows = cur.fetchall()
for row in rows:
    print(f"ID: {row[0]} | Name: {row[1]} | Phone number: {row[2]}")   
cur.close()
conn.close()