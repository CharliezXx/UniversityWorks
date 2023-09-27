ID=[]
NAME=[]

print('====part1====')
n =int(input('Enter number(1-10):'))
while n<1 or n>10:
    print('not value want...')
    n =int(input('Enter number(1-10):'))
print('====part2====')
for i in range(0,n):
    NAME.append(input('Enter String[{}]:'.format(i+1)))
    ID.append(input('Enter ID[{}]:'.format(i+1)))
print('====part3====')
print('{:15}{:20}'.format('ID','NAME'))
for j in range(0,n):
    print('{:15}{:20}'.format(ID[j],NAME[j]))
    
    
