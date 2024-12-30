def example(*args, **Kwargs):
    print("Positional arguments")
    for arg in args:
        print(arg)
    print("\nKeyword arguments")
    for key, value in Kwargs.items():
        print(f"{key} = {value}")
example(1,2,3, name = "Alice", age= 20)

def myfun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
args = ("Greeks","for","Geeks")
myfun(*args)
Kwargs = {"arg1" : "Greeks", "arg2" : "for", "arg3" : "Geeks"}
myfun(**Kwargs)

def myfun(*args, **Kwargs):
    print("args:", args)
    print("Kwargs:", Kwargs)
myfun("geeks","for","geeks", first = "Geeks", middle = "for", last = "Geeks")

class car():
    def __init__(self, *args):
        self.speed = args[0]
        self.colour = args[1]
BMW = car(200, "RED")
AUDI = car(300, "BLACK")
RANGE_ROVER = car(250, "WHITE")
FORTUNER = car(250, "WHITE")
print(FORTUNER.colour)
print(BMW.speed)
