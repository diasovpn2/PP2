import psycopg2
def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        passward="Qazmlp12",
    )