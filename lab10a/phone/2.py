from db import connect
import csv

class PhoneBook:
    def __init__(self):
        self.conn = connect()
        if not self.conn:
            exit()
        self.create_table()
    
    def create_table(self):
        """Создает таблицу phonebook если она не существует"""
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50) NOT NULL,
                    phone VARCHAR(20) NOT NULL
                )
            """)
            self.conn.commit()
    
    def insert_from_csv(self, filename):
        """Добавляет записи из CSV файла"""
        try:
            with open(filename, newline='', encoding='utf-8-sig') as f:
                reader = csv.reader(f)
                next(reader)  # Пропускаем заголовок
                with self.conn.cursor() as cur:
                    for row in reader:
                        if len(row) >= 2:  # Проверяем, что есть имя и телефон
                            self._insert_user(cur, row[0].strip(), row[1].strip())
                    self.conn.commit()
            return True
        except UnicodeDecodeError:
            print("Ошибка декодирования. Попробуйте другую кодировку, например 'cp1251'.")
            return False
        except Exception as e:
            print("Ошибка при чтении CSV:", e)
            self.conn.rollback()
            return False
    
    def _insert_user(self, cur, name, phone):
        """Вспомогательный метод для добавления пользователя"""
        cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
    
    def insert_from_input(self):
        """Добавляет запись через пользовательский ввод"""
        name = input("Введите имя: ")
        phone = input("Введите номер телефона: ")
        with self.conn.cursor() as cur:
            self._insert_user(cur, name, phone)
            self.conn.commit()
        print("Пользователь успешно добавлен.")
    
    def update_user(self):
        """Обновляет данные пользователя"""
        old_name = input("Введите имя пользователя для обновления: ")
        new_name = input("Новое имя (оставьте пустым, если не нужно менять): ")
        new_phone = input("Новый телефон (оставьте пустым, если не нужно менять): ")
        
        with self.conn.cursor() as cur:
            if new_name:
                cur.execute(
                    "UPDATE phonebook SET first_name = %s WHERE first_name = %s", 
                    (new_name, old_name)
                )
            if new_phone:
                cur.execute(
                    "UPDATE phonebook SET phone = %s WHERE first_name = %s", 
                    (new_phone, new_name or old_name)
                )
            self.conn.commit()
        print("Данные обновлены.")
    
    def search_users(self, search_type, search_term=None):
        """Поиск пользователей по различным критериям"""
        with self.conn.cursor() as cur:
            if search_type == 'all':
                cur.execute("SELECT * FROM phonebook")
            elif search_type == 'name':
                cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (search_term,))
            elif search_type == 'phone':
                cur.execute("SELECT * FROM phonebook WHERE phone = %s", (search_term,))
            elif search_type == 'pattern':
                pattern = f"%{search_term}%"
                cur.execute(
                    "SELECT * FROM phonebook WHERE first_name ILIKE %s OR phone ILIKE %s",
                    (pattern, pattern)
                )
            return cur.fetchall()
    
    def delete_user(self, delete_by, value):
        """Удаляет пользователя по имени или телефону"""
        with self.conn.cursor() as cur:
            if delete_by == 'name':
                cur.execute("DELETE FROM phonebook WHERE first_name = %s", (value,))
            elif delete_by == 'phone':
                cur.execute("DELETE FROM phonebook WHERE phone = %s", (value,))
            self.conn.commit()
        return True
    
    def close(self):
        """Закрывает соединение с базой данных"""
        if self.conn:
            self.conn.close()

def main():
    phonebook = PhoneBook()
    
    while True:
        print("\n=== ТЕЛЕФОННАЯ КНИГА ===")
        print("1. Добавить из CSV")
        print("2. Добавить вручную")
        print("3. Обновить пользователя")
        print("4. Поиск")
        print("5. Удалить пользователя")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            filename = input("Введите путь к CSV файлу: ")
            if phonebook.insert_from_csv(filename):
                print("Данные успешно импортированы!")
        
        elif choice == '2':
            phonebook.insert_from_input()
        
        elif choice == '3':
            phonebook.update_user()
        
        elif choice == '4':
            print("Тип поиска:")
            print("1. Показать всех")
            print("2. По имени")
            print("3. По телефону")
            print("4. По части имени/телефона")
            search_choice = input("Выберите тип поиска: ")
            
            if search_choice == '1':
                results = phonebook.search_users('all')
            elif search_choice == '2':
                name = input("Введите имя: ")
                results = phonebook.search_users('name', name)
            elif search_choice == '3':
                phone = input("Введите телефон: ")
                results = phonebook.search_users('phone', phone)
            elif search_choice == '4':
                pattern = input("Введите часть имени или телефона: ")
                results = phonebook.search_users('pattern', pattern)
            else:
                print("Неверный выбор")
                continue
            
            for row in results:
                print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
        
        elif choice == '5':
            print("Удалить по:")
            print("1. Имени")
            print("2. Телефону")
            delete_choice = input("Выберите тип удаления: ")
            
            if delete_choice == '1':
                name = input("Введите имя: ")
                if phonebook.delete_user('name', name):
                    print("Пользователь удален")
            elif delete_choice == '2':
                phone = input("Введите телефон: ")
                if phonebook.delete_user('phone', phone):
                    print("Пользователь удален")
            else:
                print("Неверный выбор")
        
        elif choice == '0':
            break
        
        else:
            print("Неверный выбор, попробуйте снова")

    phonebook.close()
    print("Программа завершена.")

if __name__ == "__main__":
    main()