class Zate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def getYear(self):
        return self.year
    def getMonth(self):
        if isinstance(self.month, int):
            if 0 < self.month < 13:
                return self.month
            else:
                return 'error'
    def getDay(self):
        return self.day
    

date = Zate(2007,12, 5)
print(str(date.getYear()) + "." + str(date.getMonth()) + "." + str(date.getDay()))
