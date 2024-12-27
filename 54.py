class Rectangle:
    def __init__(self, a ,b):
        self.a = a
        self.b = b
    def getSquare(self):
        self.square = self.a * self.b
        return self.square
        
    def getPerieter(self):
        self.perimeter = (self.a + self.b) * 2
        return self.perimeter
        
    def getRatio(self):
        Ratio = self.square / self.perimeter
        return Ratio
        
rectangle = Rectangle(10, 10)
print(rectangle.getSquare())
print(rectangle.getPerieter())
print(rectangle.getRatio())
