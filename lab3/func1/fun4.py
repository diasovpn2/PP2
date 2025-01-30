list=[1,2,3,4,5,6]
def num():
    u=0
    for x in range(list[u]):
        u+1
        y=x**0.5
        for i in range(2,int(y)+1):
            if x%i==0:
                print("не простое число")
            else: 
                print("простое число")
num()
