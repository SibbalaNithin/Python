my_list = [1,2,3,4,5,6]
print(len(my_list))

#range
for i in range(5):
    print(i)
    my_list.append(i)
    print(my_list)
    my_list.pop()
    print(my_list)
    my_list.reverse()
    print(my_list)


#index
mylist = ['a','b','c','d']
for index, value in enumerate(mylist):
    print(value,index)
    mylist[index] = value
    print(mylist)

#zip
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
for item1, item2 in zip(mylist1, mylist2):
    print(item1, item2)

#user defined
def demo():
    print("Hello World")
demo()

def compute(length,width):
    area = (length*width)
    print(area)
compute(15,25)

#This one is not recommended
length = 40
width = 20
def compute():
    area = length*width
    print(area)

def compute(length, width):
    area = (length*width)
    print(area)
compute(25, 2)


#LAMBDA

x = lambda a : a + 5
print(x(4))

y = lambda a, b: a * b
print(y(5,4))

z = lambda a, b, c: a*b*c
print(z(5,4,3))

z = lambda a, b, c: a+b+c
print(z(3,4,5))


def demo():
    x = lambda a : a + 5
    print(x(5))
demo()


def myfunc(n):
    return lambda a : a * n
mytriple = myfunc(3)
mydouble = myfunc(2)
print(mytriple(5))
print(mydouble(10))


print("Hello world")
print("What is your name?")
myname = input()
print("Its good to meet you" + myname)
print("The length of your name is:")
print(len(myname))
print("What is your age?")
myage = input()
print("you will be"+str((int(myage))+ 1) + "in a year")

try:
    length = 10
    width = 0
    length/width
except Exception:
    print("Division by zero is invalid! kindly change your input")

try:
    user = input("Enter your number: ")
    number = int(user_input)

    result = 10/10

    my_list = [1, 2, 3]
    element = my_list[10]

    my_dict = {'key1':'value1'}
    value = my_dict['key2']

except ValueError as ve:
    print(f"ValueError : {ve}")
except ZeroDivisonError as zde:
    print(f"ZeroDivisionError : {zde}")
except IndexError as ie:
    print(f"IndexError : {ie}")
except KeyError as ke:
    print(f"KeyError : {ke}")
else:
    print(f"Result: {result}")
finally:
    print("Execution Completed")

