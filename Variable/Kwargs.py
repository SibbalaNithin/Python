def greet(**Kwargs):
    for key, value in Kwargs.items():
        print(f"{key} says {value}")
greet(john = "Hello", kavya = "Hi", preethi = "Hey")

def myfun(**Kwargs):
    for key, value in Kwargs.items():
        print("%s == %s" % (key, value))
myfun(First = "Nithin", Middle = "Girish", Last = "Yaswanth")

def myfun(arg1,**Kwargs):
    for key, value in Kwargs.items():
        print("%s == %s" % (key, value))
myfun("Hi", first = "Nithin", middle = "Girish", last = "Yaswanth")

def myfun(arg, **Kwargs):
    for key, value in Kwargs.items():
        print("%s == %s" % (key, value))
myfun("Hello", first = "Chill", mid = "The", last = "Weekends")