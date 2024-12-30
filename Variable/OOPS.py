class calc:
    num = 100
    def getData(self):
        print("I am now executing as method in class")
obj = calc()
obj.getData()
print(obj.num)

class calc:
    num = 50
    def getData(self):
        print("I am now executing as method in class")
    #Constructor
    def __init__(self):
        print("I am noe executed first in the pgm")
obj = calc()
obj.getData()
print(obj.num)

class calc:
    num = 100
    def getData(self):
        print("I am now executing as method in class")
    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber = b
        print("I am now executed first in the pgm   ")
    def summation(self):
        return self.firstnumber + self.secondnumber + self.num
obj = calc(10,20)
obj.getData()
print(obj.num)
print(obj.summation())


class childimpl(calc):
    num2 = 200
    def __init__(self):
        calc.__init__(self,50,60)
    def getcompleteddata(self):
        return self.num2 + self.num + self.summation()
obj = childimpl()
print(obj.getcompleteddata())

class sharp:
    num = 40
    def getData(self):
        print("I am executing as method is class")
    def __init__(self,a,b):
        self.firstnumber = 10
        self.secondnumber = 30
        print("I am now executing this method only")
    def summation(self):
        return self.firstnumber + self.secondnumber + self.num
obj = sharp(10, 30)
obj.getData()
print(obj.summation())

#POLYMORPHISM
