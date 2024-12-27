class Circle:
    __radius = 0
    def setRad(self, radius):
        self.__radius = radius
        
    def showS(self):
        s = 3.14 * self.__radius * self.__radius
        return s
        
    def showLong(self):
        l = 2 * 3.14 * self.__radius
        return l
circle = Circle()
circle.setRad(5)
print(circle.showS())
print(circle.showLong())
