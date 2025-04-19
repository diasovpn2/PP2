import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="users",
        user="postgres",
        password="Qazmlp12",
        host="localhost",
        port="5432"
    )
