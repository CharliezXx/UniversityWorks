num = int(input('Enter number [3-9]: '))
for i in range (1,num+1):
    for j in range(1,i+1):
        if j==1 or j>=i:
            print(i,end='')
        elif i == num:
            print(i,end='')
        else:
            print(' ',end='')
    print('')