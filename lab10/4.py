import psycopg2
conn = psycopg2.connect(
    host = "localhost",
    dbname = "phonebook_db",
    user = "postgres",
    password = "qazplm123"   
)
cur = conn.cursor()
during = True
while during:
    name = input("Enter name: ")
    phone = input("Enter numbers of ur phone: ")
    cur.execute(
    "INSERT INTO Phonebook (name, phone) VALUES (%s, %s)" , (name, phone))
    zapros = input("Do u want to add one more?: ")
    if zapros == 'Yes' or zapros == 'yes':
        during = True
    else:
        during = False
conn.commit()
print("Contact added succesfully!")
cur.close()
conn.close()