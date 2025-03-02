import os
try:
    p=input()
    if not os.path.exists(p):
        print("Путь не существует.")
    else:
        print("Путь существует.")
        print("Читаемый:", os.access(p, os.R_OK))
        print("Записываемый:", os.access(p, os.W_OK))
        print("Исполняемый:", os.access(p, os.X_OK))
except Exception as e:
    print("Ошибка:", e)
