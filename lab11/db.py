import psycopg2

DB_CONFIG = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'Qazmlp12',
    'host': 'localhost',
    'port': '5432',
    'client_encoding': 'utf-8'  # Добавление кодировки
}

def connect():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None
