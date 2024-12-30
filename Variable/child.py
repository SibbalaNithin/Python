from OOPS import calc
class childimpl(calc):
    num2 = 200
    def __init__(self):
        calc.__init__(self,50,60)
    def getcompleteddata(self):
        return self.num2 + self.num + self.summation()
obj = childimpl()
print(obj.getcompleteddata())

from OOPS import sharp

class childimpl(sharp):
    num2 = 1000
    def __init__(self):
        sharp.__init__(self,60,60)
    def getcompleteddata(self):
        return self.num2 + self.num + self.summation()
obj = childimpl()
print(obj.getcompleteddata())