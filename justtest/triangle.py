num = int(input('Enter number [3-9]: '))
for i in range (1,num+1):
    for j in range(1,i+1):
        if j==1 or j>=i:
            print('*',end='')
        elif i == num:
            print('*',end='')
        else:
            print(' ',end='')
    print('')