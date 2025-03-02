def wr(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for i in data:
            file.write(f"{i}\n")
    print(f"List written {filename}")


wr("output.txt", ["A", "B", "C"])