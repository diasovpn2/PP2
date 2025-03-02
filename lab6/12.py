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

    list_data = ["Первая строка", "Вторая строка", "Третья строка"]
    output_file = input("Введите путь для сохранения списка: ").strip()
    with open(output_file, 'w', encoding='utf-8') as file:
        for item in list_data:
            file.write(item + "\n")
    print("Список записан в файл.")
    directory = input("Введите путь для создания файлов A-Z: ").strip()
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for char in range(65, 91): 
        file_name = os.path.join(directory, f"{chr(char)}.txt")
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f"Это файл {chr(char)}.txt\n")
    print("Файлы A-Z созданы успешно.")

    source_file = input("Введите путь исходного файла: ").strip()
    destination_file = input("Введите путь файла назначения: ").strip()
    
    if os.path.exists(source_file) and os.path.isfile(source_file):
        with open(source_file, 'r', encoding='utf-8') as src, open(destination_file, 'w', encoding='utf-8') as dest:
            dest.write(src.read())
        print("Файл успешно скопирован.")
    else:
        print("Исходный файл не существует или не является файлом.")

except Exception as e:
    print("Ошибка:", e)
