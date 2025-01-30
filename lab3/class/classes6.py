def num():
    x=int(input())
    y=x**0.5
    for i in range(2,int(y)+1):
        if x%i==0:
            print("не простое число")
            return     
    print("простое число")
num()
