class User:
    def setNickname(self, nick):
        self.nickname = nick
        
    def getNickname(self):
        return self.nickname
class Employee(User):
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
        
class Programmer(Employee):
    def setSurn(self, surname):
        self.surname = surname
        
    def getSurn(self):
        return self.surname
        
class Designer(Programmer):
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age
