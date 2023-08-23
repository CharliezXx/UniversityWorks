n = int(input('Enter a number: '))

def sum_of_n(x):
    if x > 1:
        print(x,'+',end='',sep='')
        return(x+sum_of_n(x-1))
    else:
        print(x,'= ',end='')
        return(1)

m = sum_of_n(n)
print(m)