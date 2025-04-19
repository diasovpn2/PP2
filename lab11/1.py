import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Qazmlp12"
    )

# Функция для выполнения SQL-скрипта
def ssql_script(script):
    conn = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(script)
        conn.commit()
        print("SQL скрипт выполнен успешно.")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка при выполнении SQL: {error}")
    finally:
        if conn is not None:
            conn.close()

# Функция для получения всех данных из таблицы phonebook
def get_all_records():
    conn = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM phonebook;")
        records = cursor.fetchall()
        print("Текущие записи в таблице phonebook:")
        for record in records:
            print(record)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка при извлечении данных: {error}")
    finally:
        if conn is not None:
            conn.close()

# SQL-скрипт для создания таблицы и процедур
sql_script = """
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    surname TEXT,
    phone TEXT NOT NULL
);

-- Функция для поиска по шаблону
CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(id INT, name TEXT, surname TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT id, name, surname, phone
    FROM phonebook
    WHERE name LIKE '%' || pattern || '%'
       OR surname LIKE '%' || pattern || '%'
       OR phone LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- Процедура для вставки или обновления пользователя
CREATE OR REPLACE PROCEDURE insert_or_update_user(new_name TEXT, new_phone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = new_name) THEN
        UPDATE phonebook
        SET phone = new_phone
        WHERE name = new_name;
    ELSE
        INSERT INTO phonebook (name, phone)
        VALUES (new_name, new_phone);
    END IF;
END;
$$;

-- Процедура для удаления данных по имени или телефону
CREATE OR REPLACE PROCEDURE delete_user_by_username_or_phone(identifier TEXT)
LANGUAGE plpgsql AS $$ 
BEGIN
    DELETE FROM phonebook
    WHERE name = identifier;

    IF NOT FOUND THEN
        DELETE FROM phonebook
        WHERE phone = identifier;
    END IF;
END;
$$;
"""

# Выполнение SQL-скрипта
ssql_script(sql_script)

# Добавление/обновление данных
insert_script = """
CALL insert_or_update_user('John Doe', '1234567890');
CALL insert_or_update_user('Jane Smith', '0987654321');
"""

ssql_script(insert_script)
get_all_records()
