import my_factorial
n = int(input('Enter a number (1-100): '))
while n<1 or n>100:
    print('Invalid Input!!!')
    n = int(input('Enter a number (1-100): '))
my_factorial.Fac.loop(n)
my_factorial.Fac.recursive(n)