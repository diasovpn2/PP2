from functools import reduce
def mr(n):
    return reduce(lambda x, y: x * y, n)
n = [2, 3, 4, 5]
r=mr(n)
print(r)
