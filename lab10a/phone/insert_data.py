import csv
from db import connect

def insert_from_csv(file_path):
    conn = connect()
    cur = conn.cursor()

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name, phone = row
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("Данные из CSV успешно добавлены.")

def insert_from_console():
    conn = connect()
    cur = conn.cursor()

    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("Данные успешно добавлены через консоль.")

mode = input("Выберите способ вставки (1 - CSV, 2 - Консоль): ")

if mode == "1":
    path = input("Введите путь к CSV-файлу (например, data.csv): ")
    insert_from_csv(path)
elif mode == "2":
    insert_from_console()
else:
    print("Неверный выбор.")
