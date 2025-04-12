import psycopg2

# Подключаемся к базе данных
conn = psycopg2.connect(
    host="localhost",         # База в компьютере
    dbname="phonebook_db",    # Имя базы данных
    user="postgres",          # Имя пользователя
    password="qazplm123"  #пароль
)
# Проверка соединения
print("Успешное подключение к базе данных!")
# Закрываем соединение
conn.close()