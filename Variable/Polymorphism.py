Over ridding
class Employee:
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 100
    def displaynumberofworkinghours(self):
        print(self.numberofworkinghours)

class Trainee(Employee):
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 150
    def resetnumberofworkinghours(self):
        super().setnumberofworkinghours()

emp = Employee()
emp.setnumberofworkinghours()
print("The number of working hours of employees:", end = " ")
emp.displaynumberofworkinghours

trainee = Trainee()
trainee.setnumberofworkinghours()
print("The number of working hours of employees:", end = " ")
trainee.displaynumberofworkinghours()

trainee.resetnumberofworkinghours()
print("The number of working hours has been reset:", end = " ")
trainee.displaynumberofworkinghours()