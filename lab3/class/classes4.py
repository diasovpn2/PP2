class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("кординаты",{self.x}, {self.y})
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, new_x, new_y):
        w=(self.x - new_x) ** 2 + (self.y - new_y) ** 2
        print(w**0.5)
q = Point(0,0)
q.show() 
q.dist(3,3)