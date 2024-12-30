fruits = ["apple", "pear", "orange", "banana"]
for demo in fruits:
    print(demo)

#range
for number in range(1, 10):
    print(number)


temp = 1
while temp > 1 and temp <= 1:
    print("The room temperature is maintained at {}".format(temp))

number = 1
for row in range (1,4):
    for column in range (1,4):
        print(number,end=' ')
        number = number+1
    print()

#BREAK
for number in range(1,11):
    if number == 5:
        break
    else:
        print(number)

for number in range(1,11):
    if number == 5:
        continue
    else:
        print(number)
else:
    print("All the numbers were printed")


for number in range(1,11):
    if number == 5:
        break
    else:
        print(number)
else:
    print("All the numbers were printed")


#for loop
n = 11
for i in range (1,n):
    print(i)

n = 20
for i in range(n):
    if i%2 == 0:
        print(i)

n = 10
sum = 0
for i in range(1,n+1):
    sum+=i
    print(sum)
n = 10
sum = 0
for i in range(n):
    if i%2 != 0:
        sum+=i
        print(sum)

n = 5
for i in range(11):
    print(n,"x",i,"=",5*i)

list = [2,4,6,8,0,13,45,67,89]
for i in list:
    print(i)

n = 25469871023
n = str(n)
count = 0
for i in n:
    count+=1
print(count)

given_string = "Madam"
reverse_string = ""
for i in given_string:
    reverse_string = i+reverse_string

if(given_string == reverse_string):
    print("The string",given_string,"is a palindrome.")
else:
    print("The string", given_string,"is not a palindrome.")


given_number = 153
given_number = str(given_number)
str_length = len(given_number)
sum = 0
for i in given_number:
    sum+=int(i)**str_length
if sum == int(given_number):
    print("The given number", given_number,"is an Armstrong number.")
else:
    print("The given number", given_number,"is not an Armstrong number.")


num_list = [2,5,8,6,45,25,15,65,22]
for i in num_list:
    if i%2 == 0:
        print(i,"is an even number")
    else:
        print(i,"is an odd number")

import math
def is_not_prime(n):
    flag = False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            flag = True
    return flag
range_starts = 10
range_ends = 30
print("Non-Prime numbers between",range_starts,"and",range_ends,"are:")
for number in filter(is_not_prime,range(range_starts, range_ends)):
    print(number)

n = 10
num1 = 0
num2 = 1
next_num = num2
count = 1
while count <= n:
    print(next_num, end=" ")
    count += 1
    num1, num2 = num2, next_num
    next_num = num1+num2
print()


n = 20
num1 = 0
num2 = 1
next_num = num2
count = 1
while count <= n:
    print(next_num, end=" ")
    count+=1
    num1, num2 = num2, next_num
    next_num = num1+num2
print()

given_num = 5
factorial = 1
for i in range(1,given_num+1):
    factorial = factorial*i
print("The factorial", given_num,"is", factorial)

given_range = 25
for i in range(given_range+1):
    if i % 4 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
    if i % 4 == 0 and i % 5 != 0:
        print("fizz")
        continue

    if i % 5 == 0 and i % 4 != 0:
        print("buzz")
    else:
        print(i)

month = ["January","February", "March", "April", "May", "December"]
for i in month:
    if i == "February":
        print("The month of february has 28/29 days")
    elif i in ("April","January","March","May","December"):
        print("The month of",i,"has 30 days")
    elif i in ("January","March","May","July","August","October","December"):
        print("The month of",i,"has 31 days.")
    else:
        print(i,"is not a valid month name.")