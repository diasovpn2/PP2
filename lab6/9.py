def lines(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cnt = sum(1 for _ in file)
        print(f"lines: {cnt}")

    except FileNotFoundError:
        print("file does not exist")

lines("tutu.txt")