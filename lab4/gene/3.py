def a(x):
    for i in range(1,x+1):
        if i%3==0 and i%4==0:
            yield str(i)
x=int(input())
print(" ".join(a(x)))