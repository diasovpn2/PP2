import math 
def u(x,y):
    return (x*y**2)/(4*math.tan(math.pi/x))
x=int(input())
y=int(input())
print(int(u(x,y)))