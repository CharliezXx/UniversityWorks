w = int(input('width :'))
s = int(input('stroke :'))
print('1234567890'*2)
for i in range (1,w+1):
    if i <=s or i > (w-s):
        for j in range(1,w+1):
            print('o',end='')
    elif i >=s and i <= (w-s):
        for k in range (1,w+1):
            if k <= s:
                print('o',end='')
            elif k>= (1+w-s):
                print('o',end='')
            else:
                print(' ',end='')
    print('')