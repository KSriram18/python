class Shape:
    def __init__(self):
        pass
    def area(self):
        print("Area of Shape: 0")
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        print("Area of Shape:",self.length*self.length)
box=Square(5)
box.area()     