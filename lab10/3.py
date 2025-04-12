import psycopg2
import csv

conn = psycopg2.connect(
    host = "localhost",
    dbname = "phonebook_db",
    user = "postgres",
    password = "qazplm123"   
)
cur = conn.cursor()
file ="lab10/first task/contacts.csv"
with open(file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    
    for row in reader:
        name, phone = row
        cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
conn.commit()
print("Contact added succesfully!")
cur.close()
conn.close()