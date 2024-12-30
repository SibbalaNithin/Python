totalmarks = 95
if totalmarks >=96:
    print("congrats you have secured a 'A' grade")
else:
    print("Sorry you have not secured a 'A' grade")


totalmarks = 60
if totalmarks >= 70:
    print("congrats you have secured a 'A' grade")
elif totalmarks >= 40:
    print("congrats you have cleared the exam")
else:
    print("you failed the exam")

totalmarks = 90
if totalmarks <= 90:
    print("congrats you have secured a 'A' grade")
elif totalmarks >= 60:
    print("you have cleared the exam")
else:
    print("you failed the exam")


totalmarks = 100
if totalmarks >= 90:
    print("congrats you have secured a 'A' grade")
    if totalmarks == 100:
        print("congrats you have secured a 'A+' grade")
else:
    print("you failed the exam")


a = 10
b = 5

if a > b:
    print("a greater than b")
else:
    print("a less than b")


a = 200
b = 200
if a != b:
    print("a is greater than b")
elif a == b:
    print("b is equal to a")
else:
    print("b is less than b")


a = 20
b = 20
if a == b: print("a is equal to b")


totalmarks = 95
attendance = 97
percentage = 94
if (totalmarks >= 92 or attendance == 98) and percentage >= 93:
    print("You are a good student")
else:
    print("You are a bad student")


fruit = 'Apple'
if fruit is "Mango" and fruit is "Apple":
    print("I love that fruit")