class Shape():
    def area(self):
        return 0
class Square(Shape):   
    def __init__(self,x):
        self.x=x
    def area(self):
        return self.x*self.x
x=int(input("введите число: "))
w=Square(x)
q=Shape()
print("площадь квадрата",w.area())
print("по умолчанию",q.area())