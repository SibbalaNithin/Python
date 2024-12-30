def add(*args):
    total = 0
    for num in args:
        total += num
    return total
print(add(1,2))
print(add(2,3,4,5,6,7,8))

def myfun(*args):
    for i in args:
        print(i)
myfun("Hello","Welcome","to","Python class")

def myfun(arg1, *argv):
    print("First argument:", arg1)
    for arg in argv:
        print("Next argument through *argv:", arg)
myfun("Hello","Welcome", "to", "Python", "Class")

def myfun(arg1, *argv):
    print("First argument:", arg1)
    for arg in argv:
        print("Next argument through a argv:", arg)
myfun("HEY", "Welcome", "to", "this", "Session")

