from db import connect
conn=connect()
cun=conn.cursor()
cun.execute("""
            UPDATE  phonebook
            SET phone=+7|| SUBSTR(phone,3)
            WHERE phone LIKE '8%'
            """
)
conn.commit()
print("good")
cun.close()
conn.close()