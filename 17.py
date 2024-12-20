class Employee:
    __name = None
    __salary = 0 
    __age = 0
    
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age
    
    def setSalary(self, salary):
                self.__salary = salary
        
    def setName(self, name):
                self.__name = name
    
    def setage(self, age):
                self.__age = age

    def getSalary(self):
        return self.__salary
        
    def getName(self):
        return self.__name.upper
    
    def getage(self):
        return self.__age
    


employee = Employee('','','')
employee.setName  = 'Max'
employee.setSalary = 45632
employee.setage = 37
print(employee.getSalary())
print(employee.getage())
print(employee.getName())
