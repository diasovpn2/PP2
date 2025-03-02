import os

try:
    path = input("Введите путь: ").strip()
    
    if not os.path.exists(path):
        print("Путь не существует.")
    else:
        print("Путь существует.")
        print("Читаемый:", os.access(path, os.R_OK))
        print("Записываемый:", os.access(path, os.W_OK))
        print("Исполняемый:", os.access(path, os.X_OK))
        print("Имя файла:", os.path.basename(path))
        print("Директория:", os.path.dirname(path))
        
        if os.path.isfile(path):
            with open(path, 'r', encoding='utf-8') as file:
                line_count = sum(1 for _ in file)
            print("Количество строк в файле:", line_count)
except Exception as e:
    print("Ошибка:", e)