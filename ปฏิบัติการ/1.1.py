w = int(input("width : "))
print('1234567890')
for i in range(1, w+1):
    if i == 1 or i == w:
        for n in range (1,w+1):
            if n ==w :
                print('*')
            else:
                print('*',end='')
    else:
        for y in range(1,w+1):
            if y == 1:
                print('*',end='')
            elif y== w:
                print('*')
            else:
                print(' ',end='')