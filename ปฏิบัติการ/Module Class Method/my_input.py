def get(y,z):
    x = int(input('Enter a number ({}-{}): '.format(y,z)))
    while x<y or x>z:
        print('Invalid number!!!')
        x = int(input('Enter a number ({}-{}): '.format(y,z))) 
    print('You entered number',x)