def a(x):
    for i in range(2,x+1,2):
        yield str(i)
x=int(input())
print(",".join(a(x)))