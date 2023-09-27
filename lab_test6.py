print('=== part 1 ===')
n = int(input('How many number(2-10) : '))
while n<2 or n>10:
    print('Try again')
    n = int(input('How many number(2-10) : '))
name =[]
last_name =[]
print('OK')

print('=== part 2 ===')
for i in range (0,n):
    s = input('Name {} : '.format(i+1))
    name.append(s)
    s = s.split()
    last_name.append(s[1])

print('=== part 3 ===')
for j in range(0,len(name)):
    
    print('Name {} : {}'.format(j+1,name[j]))
    print('Last name is {}'.format(last_name[j]))
    print('Number of Last',len(last_name[j]))