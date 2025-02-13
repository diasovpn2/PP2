lis = [1, 2, 3, 4, 5, 6]
def num():
    for x in lis:
        if x < 2:
            print(x, "— не простое число")
            continue
        count = 0
        for i in range(1, x + 1):
            if x % i == 0:
                count += 1
        if count == 2:
            print(x, "— простое число")
        else:
            print(x, "— не простое число")
num()
