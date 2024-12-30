#Looping
for i in range (1, 11):
    print(i)

#Conditional statements
a = int(input("Enter a number:" ))
for i in range (15):
    if a == 15:
        print("Positive")
    elif a == (-15):
        print("Negative")
    else:
        print("Zero")

a = int(input("Enter a number: "))
if a >= 0:
    if a == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")

#Looping and Conditional Statements
i = 2
while i <= 20:
    print(i)
    i += 2
if i in range (1, 21, 2):
    print(i)
#Factorial
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return(n * factorial(n-1))
num = 0
print("number: ", num)
print("Factorial: ", factorial(num))
