n = eval(input('Enter a number: '))
for i in range(1, n+1):
    for j in range(1, n+1):
        print('*', end=' ')
    print()

n = eval(input('Enter a number: '))
for i in range(1, n+1):
    for j in range(1, i+1):
        print('*', end=' ')
    print()

n = eval(input('enter a number:'))
for i in range(1, n+1):
    for j in range(1, i-1):
        print('*', end=" ")
    print()
    for j in range(1, n+1):
        print('*', end=' ')
        print()

n = eval(input("Enter a number: "))
for i in range(1,n+1):
    for i in range(i,n+2):
        print('*',end='')
    print()

n = eval(input('Enter a number: '))
for i in range(1, n+1):
    for j in range(1, n+1-i):
        print(' ',end='')
    for k in range(1,i+1):
        print('*',end='')
    print()
