
def dec_2_oct(x):
    if x>1:
        dec_2_oct(x//8)
    else:
        return()
    print(x%8,end='')
    return ''

n = int(input('Enter an integer: '))

print('Decimal {} = '.format(n),end='')
z = dec_2_oct(n)
print(' Octal')