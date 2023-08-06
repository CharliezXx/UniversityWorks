odd = False
while odd == False:
    n = int(input('Enter an odd base (3-9):'))
    if n%2 == 1 and not n>=10 and not n<3:
        odd = True
    else:
        print('Invalid number!!!\nThe number must be an odd number from 3 to 9.')
count = 1
mid = int((1+n)/2)
m=1
while count !=n+1:
    if count <= mid:
        for i in range (0,count):
            print(count,end='')
        print()
    else:
        for j in range(mid-m,0,-1):
            print(count,end='')
        print()
        m +=1
    count +=1
    

    
    
    