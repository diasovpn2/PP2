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
except Exception as e:
    print("Ошибка:", e)