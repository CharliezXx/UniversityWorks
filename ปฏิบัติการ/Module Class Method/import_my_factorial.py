import my_factorial
n= int(input('Enter a number(1-100):'))
while n<1 or n>100:
    n= int(input('Invalid number!!!\nEnter a number(1-100):'))
my_factorial.Fac.loop(n)
print('Calculator Factorial Using Recursion\n{}! = '.format(n),end='')
print(my_factorial.Fac.recursive(n))