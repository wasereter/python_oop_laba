class Employee:
    __name = None
    __salary = 0
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

class EmployeesCollection:
    def __init__(self):
        self.__name = []
        self.__salary = []
    def add(self, name, salary):
        self.__name.append(name)
        self.__salary.append(salary)
    def show(self):
        for name in self.__name:
            print(name)
        for salary in self.__salary:
            print(sum(salary))
    def midsalary(self):
        print(sum(salary)/len(self.__name))
uc = EmployeesCollection
uc.add('john', 242423)
uc.add('eric', 42121) 
uc.add('kyle', 31231)
us.show
