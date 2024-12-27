class User:
	__name = ''

	def setName(self, name):
		self.__name = name

	def getName(self):
		return self.__name

class Employee(User):
    __name = ''
    def __init__(self):
        __name = self.getName()
	
    def setName(self, name):
        if (len(self.__name) > 0):
            self.__name = self.__name
            
    def getName(self):
        return self.__name

employee = Employee()
employee.setName('Jon')
print(employee.getName())
