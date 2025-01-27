class Rectangleclass():
    def area(self):
        return 0
class Square(Rectangleclass):   
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
x=int(input("введите число: "))
y=int(input("введите число: "))
w=Square(x,y)
q=Rectangleclass()
print("площадь квадрата",w.area())
