import my_factorial
n = int(input('Enter a number (1-100):'))
while n<1 or n>100:
    print('Invalid number!!!')
    n = int(input('Enter a number (1-100):'))
print(my_factorial.Fac.loop(n))
print(my_factorial.Fac.recursive(n))