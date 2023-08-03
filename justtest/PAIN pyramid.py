odd = False
row=0
while odd == False:
    n = int(input('Enter an odd base (3-9):'))
    if n%2 == 1:
        odd = True
    else:
        print('Invalid number!!!\n The number must be an odd number from 3 to 9.')
 
count = 1       
for i in range (1,n+1):
    if i%2 == 1:
        row +=1
    
for j in range (1,row+1):
    print('Row {} ->  '.format(j),end='')
    for k in range(1,row):
        print(' ',end='')
    if row == 1:
        for l in range (1,count+1):
            print(l,end='')
    else:
        for l in range (1,count+1):
            print(l+k,end='')
    count += 2
    row -=1
    print()
    
    
        