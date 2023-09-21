print('--- Part 1 ---')
n = int(input('How many name (3-7): '))
while n>7 or n<3:
    if n>7:
        print('To big!')
    else:
        print('To little')
    n = int(input('How many name (3-7): '))
print("--- Part 2 ---")
s =[]
temp=''
for i in range(0,n):
    x = input('Name {} = '.format(i+1))
    s.append(x)
print('Name =',s,'\n--- Part 3 ---')
for j in range(0,len(s)):
    temp += s[j]
    l,d = 0,0
    for k in range(0,len(temp)):
        if temp[k].islower():
            l+=1
        if temp[k].isdigit():
            d+=1
    print('Name {} ==> {}'.format(j+1,s[j]))
    if d !=0:
        print('     Total {} digit character'.format(d))
    else:
        print('     Contain no digit character')
    if l !=0:
        print('     Total {} lower-case character'.format(l))
    else:
        print('     Contain no lower-case character')
    temp=''
    
    